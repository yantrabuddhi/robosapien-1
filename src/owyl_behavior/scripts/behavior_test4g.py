#! /usr/bin/env python
__author__ = 'mandeep'
import rospy
import owyl
from owyl import blackboard
from std_msgs.msg import Bool
from std_msgs.msg import String
from std_msgs.msg import Int32
#from std_msgs.msg import Char .. has bug in ros implementation
from vision.msg import face_box
from vision.msg import targets
from tld_msgs.msg import BoundingBox
from tld_msgs.msg import Target
from sensor_msgs.msg import Image
from std_msgs.msg import Float32MultiArray
#import math
#import cv
#from cv_bridge import CvBridge, CvBridgeError
# reset tld tracker each time track command is given or subject is lost or low confidence for a few seconds
#cmds std_msgs::Char ... keep global instead of local private topic as may need to reset without publishing too many topics
#maybe modify cmds later to allow choosing the subscriber
#        case 'b':
#          clearBackground();
#        case 'c':
#          stopTracking();
#        case 'l':
#          toggleLearning();
#        case 'a':
#          alternatingMode();
#        case 'e':
#          exportModel();
#        case 'i':
#          importModel();
#        case 'r':
#          reset();
#from tld_msgs.msg import Target
from robot.msg import robot_cmd
from robot.msg import compass #not available for ITF Demo due to gesture R
from robot.msg import sonar
from robot.msg import gesture_r
stt_cmd_map= {
             "BADINPUT":(0,0,""),
             "walk forward":(1,400,"walk forward"),#body class,800*10 ms timer,command for body
             "walk back":(1,400,"walk backward"),
             "turn":(1,400,"turn left"),
             "turn right":(1,400,"turn right"),
             "look up":(2,400,"t+"),#tilt up
             "look down":(2,400,"t-"),
             "look like":(2,400,"p+"),#pan,400*10ms,left .. word left not recognized
             "look left":(2,400,"p+"),#pan,400*10ms,left .. word left not recognized
             "look right":(2,400,"p-"),
             "look center":(2,400,"tp"),
             "give faces":(3,500,"faces"),#test speech active?
             "give distance":(3,500,"sonar"),
             "give heading":(3,500,"compass"),#
             "track me":(4,400,"friend"),
             #"track object":(4,400,"object")
             "identify":(5,400,"id objects")#recognize
}
tts_objects_map={"1":"book",
                 "2":"box"}
#object images in ~/objects/
trackers={"face":BoundingBox(),
          "object":BoundingBox()}#use confidence value while tracking
class body_cmd:
    def __init__(self,blackboard):
        self.bb=blackboard

class behavior:
    def __init__(self,bb):
        self.blackboard=bb#blackboard.Blackboard("behavior")
        #rospy.loginfo (self.blackboard["stt"])
        self.main_tree=self.create_main_tree()
        #while not rospy.is_shutdown():
        #    self.main_tree.next()

    def create_main_tree(self):
        tree=owyl.repeatAlways(
                owyl.sequence(
                    self.poll_tracking(),
                    self.is_stt_on(),
                    self.poll_gesture(),
                    self.is_stt_done(),
                    owyl.selector(
                        self.run_stt_command(),
                        self.run_stt_chat()
                    )
                )
        )
        return owyl.visit(tree,blackboard=self.blackboard)

    def pan_right(self,deg):
        pa=rospy.get_param("/robot/get_pan")
        pn=pa-deg
        v=Int32(pn)
        self.blackboard["pub_pan"].publish(v)

    def pan_left(self,deg):
        pa=rospy.get_param("/robot/get_pan")
        pn=pa+deg
        v=Int32(pn)
        self.blackboard["pub_pan"].publish(v)

    def tilt_down(self,deg):
        pa=rospy.get_param("/robot/get_tilt")
        pn=pa-deg
        v=Int32(pn)
        self.blackboard["pub_tilt"].publish(v)

    def tilt_up(self,deg):
        pa=rospy.get_param("/robot/get_tilt")
        pn=pa+deg
        v=Int32(pn)
        self.blackboard["pub_tilt"].publish(v)

    @owyl.taskmethod
    def poll_tracking(self,**kwargs):
        img_width=640
        img_height=480
        tt=self.blackboard["to_track"]
        if tt in self.blackboard["trackers"] and self.blackboard["track_delay"]<1:
            trk=self.blackboard["trackers"][tt]
            if trk.confidence>0.2:#0.4
                if trk.x<(img_width/2)-(img_width/5):#4 was previous
                    self.pan_left(2)
                    self.blackboard["track_delay"]=100/10
                if trk.x>(img_width/2)+(img_width/5)-(trk.width/2):
                    self.pan_right(2)
                    self.blackboard["track_delay"]=100/10
                if trk.y<(img_height/2)-(img_height/5):
                    self.tilt_up(2)
                    self.blackboard["track_delay"]=100/10
                if trk.y>(img_height/2):#+(img_height/5)-(trk.height/2):
                    self.tilt_down(2)
                    self.blackboard["track_delay"]=100/10
        yield True

    @owyl.taskmethod
    def is_stt_on(self,**kwargs):
        #if self.blackboard["stt_counter"]<=0 and (not self.blackboard["speech_active"]):
        #self.b_update_bb()
        #rospy.loginfo(" stop counter="+str(self.blackboard["stop_counter"]))
        if self.blackboard["stop_counter"]<=0:
            #rospy.loginfo("ready..")
            yield True
        else:
            #rospy.loginfo("waiting...")
            yield False

    @owyl.taskmethod
    def is_stt_done(self,**kwargs):
        if self.blackboard["stt_read"]==False:
            rospy.loginfo (self.blackboard["stt"])
            self.blackboard["stt_read"]=True
            yield True
        else:
            yield False

    @owyl.taskmethod
    def poll_gesture(self,**kwargs):
        ges=self.blackboard["gesture"]
        if not(ges.direction=='o'):
            r_cmd=robot_cmd()
            todo="left hand sweep"
            r_cmd.cmd=todo
            r_cmd.duration_10ms=0
            if ges.direction=='l':
                todo="left hand strike 1"#"left hand sweep"
            elif ges.direction=='r':
                todo="right hand strike 1"#right hand sweep

            #if ges.direction=='t':
                #arm down
                #arm up
            #elif ges.direction=='b':
                #arm up
                #arm down
            #elif ges.direction=='l':
                #swipe left
            #elif ges.direction=='r':
                #swipe right
            #later do action sequences
            r_cmd.cmd=todo
            self.blackboard["wake_up_time"]=6000 #60 seconds
            self.blackboard["pub_move"].publish(r_cmd)
            self.blackboard["stop_counter"]=400
            self.blackboard["gesture"].direction='o'
        yield True

    @owyl.taskmethod
    def run_stt_command(self,**kwargs):
        #rospy.loginfo("processing stt= "+self.blackboard["stt"])
        if self.blackboard["stt"] in stt_cmd_map:
            if not(self.blackboard["stt"]=="BADINPUT"):
                rospy.loginfo("processing stt= "+self.blackboard["stt"])
                self.stt_cmd(self.blackboard["stt"])
            yield True
        else:
            yield False

    @owyl.taskmethod
    def run_stt_chat(self,**kwargs):
        self.blackboard["pub_chat"].publish(self.blackboard["stt"])
        yield True #needs to run last with zeno dial

    def stt_cmd(self,stt):
        func=stt_cmd_map[stt]
        tp=func[0]
        if not (tp==4):self.blackboard["to_track"]="null"
        self.blackboard["stop_counter"]=func[1]
        todo=func[2]
        if tp==1:
            rospy.loginfo("move bot ="+todo)
            self.blackboard["wake_up_time"]=6000 #60 seconds
            r_cmd=robot_cmd()
            r_cmd.cmd=todo
            r_cmd.duration_10ms=0
            self.blackboard["pub_move"].publish(r_cmd)
        elif tp==2:
            if todo=="t+" or todo=="t-":
                ta=rospy.get_param("/robot/get_tilt")
                tlt=0
                if todo=="t+":tlt=ta+5
                else:tlt=ta-5
                v=Int32(tlt)
                self.blackboard["pub_tilt"].publish(v)
            elif todo=="p+" or todo=="p-":
                pa=rospy.get_param("/robot/get_pan")
                pn=0
                if todo=="p+":pn=pa+5
                else:pn=pa-5
                v=Int32(pn)
                self.blackboard["pub_pan"].publish(v)
            else:
                v=Int32(45)
                self.blackboard["pub_pan"].publish(v)
                self.blackboard["pub_tilt"].publish(v)
        elif tp==3:
            to_say="What"
            if todo=="faces":
                to_say="I saw "+str(self.blackboard["num_faces"])+" faces" #bugfix
            elif todo=="sonar":
                to_say=str(board["sonar_cm"])+" centimeters"
            elif todo=="compass":
                to_say=str(board["compass_deg"])+" degrees"
            self.blackboard["pub_speak"].publish(to_say)
        elif tp==4:
            see_it=False
            if todo=="friend":
                self.blackboard["tracker_watch"]=900
                self.blackboard["to_track"]="face"
                if self.blackboard["face_memory"]>0:see_it=True
            elif todo=="object":
                self.blackboard["tracker_watch"]=900
                self.blackboard["to_track"]="object"
            #reset=String()
            #reset.data="r"
            #self.blackboard["pub_cmd"].publish(reset)#reset
            to_say="I can't see proper"
            if see_it:
                self.blackboard["pub_bb"].publish(self.blackboard["Target"])
                to_say="tracking "+todo

            self.blackboard["pub_speak"].publish(to_say)
        elif tp==5:
            see_ob=False
            if todo=="id objects":
                if self.blackboard["objects_memory"]>0:see_ob=True
            to_say="I can't see objects"
            if see_ob:
                to_say="I see "+str(self.blackboard["num_objects"])+" objects"
                self.blackboard["pub_speak"].publish(to_say)
                to_say="the objects are"
                self.blackboard["pub_speak"].publish(to_say)
                for a in self.blackboard["object_id_list"]:
                    to_say=tts_objects_map[a]
                    self.blackboard["pub_speak"].publish(to_say)
            else:
                self.blackboard["pub_speak"].publish(to_say)



def set_speech(dat):
    if board["stt_read"]:
        board["stt"]=dat.data
        rospy.loginfo("Heard : "+board["stt"])
        board["stt_read"]=False


def set_sonar(dat):
    board["sonar_cm"]=dat.distance_cm

def set_compass(dat):
    board["compass_deg"]=dat.heading_deg

def update_bb():
    #read decrement counter
    if board["stop_counter"]>0:
        board["stop_counter"]=board["stop_counter"]-1
        if board["stop_counter"]==0:
            #publish stop,
            stp_cmd=robot_cmd()
            stp_cmd.cmd="stop"
            stp_cmd.duration_10ms=0
            pub_move.publish(stp_cmd)
            #reset num faces seen
    #when 0 watchdog and low confidence discard bb, reset
    cnt=board["tracker_watch"]
    if cnt>0:
        cnt=cnt-1
    #else:
    #    board["to_track"]="null"
    if board["to_track"]=="null":cnt=0
    board["tracker_watch"]=cnt

    cnt=board["track_delay"]
    if cnt>0:
        cnt=cnt-1
    board["track_delay"]=cnt

    cnt=board["wake_up_time"]
    if cnt>0:
        cnt=cnt-1
    else:
        r_cmd=robot_cmd()
        #r_cmd.cmd="wake up" #uses too much power causes reset.. to be fix in ckt
        r_cmd.cmd="stop"
        r_cmd.duration_10ms=0
        board["pub_move"].publish(r_cmd)
        cnt=6000 #60 seconds
    board["wake_up_time"]=cnt

    cnt=board["face_memory"]
    if cnt>0:
        cnt=cnt-1
    board["face_memory"]=cnt

    cnt=board["objects_memory"]
    if cnt>0:
        cnt=cnt-1
    board["objects_memory"]=cnt


def callback_objects(data):
    arr=data.data
    num=len(arr)/12
    if num==0: return
    board["num_objects"]=num
    board["objects_memory"]=100
    board["object_id_list"]=[]
    for n in range(0,num):
        board["object_id_list"].append(str(int(arr[n*12])))

def get_faces(boxes):
    board["num_faces"]=len(boxes.faces)
    idist=0#len(boxes.faces)/2
#    cent=0.5
#    idist=0
#    td=2.0
#    din=0
#    for fc in boxes.faces:
#        dx=(0.5-fc.top_left.x+fc.width_height.x/2.0)
#        dx2=dx*dx
#        dy=(0.5-fc.top_left.y+fc.width_height.y/2.0)
#        dy2=dy*dy
#        dist=(math.sqrt(dx2+dy2))
#        if dist<td:idist=din
#        din=din+1
    tgt=Target()
    #bridge=CvBridge()
    #source=bridge.imgmsg_to_cv2(board["img"],"bgr8")

    #tgt.img=source
    tgt.img=board["img"]#.deepcopy or .copy
    bb=BoundingBox()
    bb.x=(boxes.faces[idist].top_left.x)*640
    bb.y=(boxes.faces[idist].top_left.y)*480
    bb.width=boxes.faces[idist].width_height.x*640
    bb.height=boxes.faces[idist].width_height.y*480
    bb.confidence=1.0
    bb.tracker_id="face"
    tgt.bb=bb
    board["Target"]=tgt
    board["face_memory"]=50# = 1/2 sec

def tld_tracker(box):
    #reset watchdog, store tracked data in appropriate location
    name=box.tracker_id
    confd=box.confidence
    #if name==board["to_track"] and confd>0.4:board["tracker_watch"]=900 #9 seconds
    if name==board["to_track"] :board["tracker_watch"]=60000 #60 seconds
    if name in trackers:
        board["trackers"][name]=box #watchdog set

def callback_img(data):
    #data is Image
    board["img"]=data

def callback_gesture(data):
    if board["gesture"].direction=='o':
        board["gesture"]=data
#run ant again
#/ZenoDial/output_text, zenodial.java, output.java
#/ZenoDial/text_input
#/facedetect -- face detector
#.. to add also pub and subscribe for

#map zenodial output directly to itf_talk
#upload changes to zenodial+robot, launch with ant ZenoDial
#connect speech active and enable listen

if __name__=="__main__":
    rospy.init_node("RS1_behavior")
    #subscribe to distance, compass, face bound box, objects models to be loaded
    board=blackboard.Blackboard(value="behavior")
    board["wake_up_time"]=6000 # 60 seconds
    board["stt"]=""
    board["stt_read"]=True
    board["stop_counter"]=0
    board["sonar_cm"]=0
    board["compass_deg"]=0
    board["num_faces"]=0
    board["trackers"]=trackers
    board["tracker_watch"]=0
    board["to_track"]="null"
    board["track_delay"]=0 #delay motor movement commands about 1/2 sec or 1/4 sec
    board["face_memory"]=0
    #board["face_seen"]=face_box()
    board["img"]=Image()
    board["Target"]=Target()
    ges=gesture_r()
    ges.direction='o'
    board["gesture"]=ges
    board["num_objects"]=0
    board["object_id_list"]=[]
    board["objects_memory"]=0
    rospy.Subscriber("/sense/robot/get_sonar_cm",sonar,set_sonar)
    rospy.Subscriber("/sense/robot/get_compass_deg",compass,set_compass)
    rospy.Subscriber("/sense/stt/get_text",String,set_speech)
    rospy.Subscriber('/facedetect',targets,get_faces)
    rospy.Subscriber('/tld_tracked_object',BoundingBox,tld_tracker)
    rospy.Subscriber("/cv_camera/image_raw",Image,callback_img)
    rospy.Subscriber("/sense/robot/get_gesture",gesture_r,callback_gesture)
    rospy.Subscriber("/objects",Float32MultiArray,callback_objects)
    pub_enable_listen=rospy.Publisher("/sense/stt/set_listen_active", Bool,queue_size=1)
    board["pub_enable_listen"]=pub_enable_listen
    pub_speak=rospy.Publisher("/act/tts/set_text", String,queue_size=1)
    board["pub_speak"]=pub_speak
    pub_move=rospy.Publisher("/act/robot/send_move_command", robot_cmd,queue_size=1)
    board["pub_move"]=pub_move
    pub_pan=rospy.Publisher("/act/robot/set_pan_angle", Int32,queue_size=1)
    board["pub_pan"]=pub_pan
    pub_tilt=rospy.Publisher("/act/robot/set_tilt_angle",Int32,queue_size=1)
    board["pub_tilt"]=pub_tilt
    pub_chat=rospy.Publisher("/ZenoDial/text_input",String,queue_size=1)
    board["pub_chat"]=pub_chat
    pub_cmd=rospy.Publisher("/tld_gui_cmds",String,queue_size=1)
    board["pub_cmd"]=pub_cmd
    pub_bb=rospy.Publisher("/tld_gui_bb",Target,queue_size=1)
    board["pub_bb"]=pub_bb

    be=behavior(board)
    be_tree=be.main_tree
    rate=rospy.Rate(100)#100hz
    while not rospy.is_shutdown():
        update_bb()
        be_tree.next()
        rate.sleep()
    rospy.loginfo("bye")
