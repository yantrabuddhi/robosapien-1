#!/usr/bin/env python

import owyl
from owyl import blackboard
import rospy
import numpy as np
from utils import clamp, waitForBT,delay
from std_msgs.msg import String
from std_msgs.msg import Int32
from vision.msg import targets
from robot.msg import robot_cmd
from robot.msg import sonar
from robot.msg import compass

class behavior:
    def __init__(self,bb):
        self.blackboard=bb#blackboard.Blackboard("behavior")
        #rospy.loginfo (self.blackboard["stt"])
        self.main_tree=self.create_main_tree()
        #while not rospy.is_shutdown():
        #    self.main_tree.next()
        self.Error2=5
        self.cameraSettleTolerance=100
        self.bodySettleTolerance=2
    def create_main_tree(self):
        tree=owyl.repeatAlways(owyl.sequence(self.isCameraTrack(),self.isBodyTrack(),self.isWalkForward()))
        return owyl.visit(tree,blackboard=self.blackboard)
    
    def clamp(self,low, value, high):
        return max(min(high,value),low)

    def waitForBT(self):
        print "Waiting for bluetooth to connect..."
        time.sleep(6)
        print "Connected"
    def delay(self,t_sec):
        time.sleep(t_sec)    

    @owyl.taskmethod
    def isCameraTrack(self,**kwargs):
        #rospy.loginfo("I'm in camera track mode")
        if len(self.blackboard["angles"]["pan"])<self.cameraSettleTolerance:
            # not enough data yet to decide wheter camera has settled or not!
            rospy.loginfo("publishing")
            self.CT()
            yield False
        else:
            
            self.Mean=np.mean(self.blackboard["angles"]["pan"][-5:-1])
            # rospy.loginfo("This is the mean" + str(Mean))
            self.check1=(self.blackboard["angles"]["pan"][-1]) + self.Error2
            self.check2=(self.blackboard["angles"]["pan"][-1]) - self.Error2
            # check if pan angles has settled (in effect camera track has settled)
            if self.Mean<=self.check1 and self.Mean>=self.check2:
                # clearFlags()
                #record heading degrees right after the end of camera tracking
                self.blackboard["bodyPose"].append(self.blackboard["angles"]["pan"][-1]-45)
                self.blackboard["HeadingAfterCT"].append(self.getCompass()[-1])
                # Camera Track done!
                #rospy.loginfo("Done with CT")
                yield True
            else:
                # Camera hasn't settled yet..... set busy flag
                self.CT()
                yield False
        #yield True
    
    @owyl.taskmethod
    def isBodyTrack(self, **kwargs):
        #rospy.loginfo("I'm in Body Track mode")
        bodyPose=self.blackboard["bodyPose"][0]
        heading=self.getCompass()
       
        # bodyToGo=heading[-1]-self.getHeadingCT()
        drift=heading[-1]-self.getHeadingCT()
        rospy.loginfo("bodyPose= %f,  CH= %f, ref= %f, drift= %f",bodyPose,heading[-1],self.getHeadingCT(),drift)
        if abs(drift)<abs(bodyPose):
            # Body has to got rotate some degree yet
             
            if bodyPose >=0:
                direction='turn left'
            else:
                direction='turn right'
            self.blackboard["robot_cmd_pub"].publish(direction,120)
            delay(2.0)
            yield False
            # rospy.loginfo("working on turning on the body")
        else:
            # if the drift of compass is in range,  Done with BodyTrack
            rospy.loginfo("Drift is correct")
            yield True
    @owyl.taskmethod
    def isWalkForward(self, **kwargs):
        self.pan_head(45)
        delay(0.5)
        self.tilt_head(45)
        delay(0.5)
        self.blackboard["robot_cmd_pub"].publish('walk forward',250)
        self.reintialize()
        yield True


    # return all values to default to restart the whole process of tracking again   
    def reintialize(self):
        self.blackboard["angles"] = {"pan" :[45], "tilt" :[45]}
        self.blackboard["sonar_data"] = {"distance" : [200]}
        self.blackboard["compass_data"]={"heading":[0]}
        self.blackboard["bodyPose"]=[]
    def CT(self):
        self.pan_head(self.blackboard["angles"]["pan"][-1])
        delay(1.2)
        self.pan_head(self.blackboard["angles"]["pan"][-1])
        delay(1.2)

    def pan_head(self,angle):    
        if not rospy.is_shutdown():
            self.blackboard["pan_angle_pub"].publish(angle)

    def tilt_head(self,angle):
        if not rospy.is_shutdown():
            self.blackboard["tilt_angle_pub"].publish(angle) 

    def stop_movement():
        if not rospy.is_shutdown():
            self.blackboard["robot_cmd_pub"].publish('stop', 0)

    
    def getSonarDistance(self):
        return self.blackboard["sonar_data"]["distance"]
    def getCompass(self):
        return self.blackboard["compass_data"]["heading"]
    def getHeadingCT(self):
        return self.blackboard["HeadingAfterCT"][0]




def faceDetected(boxes):
    face_left = boxes.faces[0].top_left.x
    face_top = boxes.faces[0].top_left.y
    face_width = boxes.faces[0].width_height.x
    face_height = boxes.faces[0].width_height.y

    # Calculate correction
    ideal_left = 0.5 - face_width / 2.0
    correction_pan = (ideal_left - face_left) * 2.5

    ideal_top = 0.5 - face_height / 2.0
    correction_tilt = (ideal_top - face_top) * 2.5

    temp1=board["angles"]["pan"][-1] + correction_pan
    temp2=board["angles"]["tilt"][-1]- correction_tilt

    # Clamp pan and tilt angles
    board["angles"]["pan"].append(clamp(0, temp1, 90))
    board["angles"]["tilt"].append(clamp(0, temp2, 90))

        #publish the new angles
        
            # pan_head(angles["pan"][-1])
            # tilt_head(angles["tilt"][-1])
            # clearFlags()
def readSonarDist(data):
    board["sonar_data"]["distance"].append(data.distance_cm)

def readCompass(data):
    board["compass_data"]["heading"].append(data.heading_deg)
    
    

    

if __name__=="__main__":
    TOLERANCE = 15
    Error= 2
    Error2=5
    # Init Node
    rospy.init_node('behavior', anonymous = False)

    # Init publishers
    board=blackboard.Blackboard()
    pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 1)
    tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 1)
    robot_cmd_pub = rospy.Publisher('/act/robot/send_move_command', robot_cmd, queue_size = 1)
    board["pan_angle_pub"]  = pan_angle_pub
    board["tilt_angle_pub"] = tilt_angle_pub
    board["robot_cmd_pub"]  = robot_cmd_pub
    # Wait for bluetooth to connect
    waitForBT()

    # Init variables
    board["angles"] = {"pan" :[45], "tilt" :[45]}
    board["sonar_data"] = {"distance" : [200]}
    board["compass_data"]={"heading":[0]}
    board["bodyPose"]=[]

    # This records the heading right after the camera track has stopped
    board["HeadingAfterCT"]=[]
    #defines the current state of the robot
    # flags = {"turn left" : False, "turn right" : False, "walk forward" : False,"Camera track":False,"Body track":False,"follwing":False}  

    # Move head to default position
    rospy.Subscriber('facedetect', targets, faceDetected)
    rospy.Subscriber('/sense/robot/get_sonar_cm', sonar, readSonarDist)
    rospy.Subscriber('/sense/robot/get_compass_deg',compass,readCompass)
    

    be=behavior(board)
    be_tree=be.main_tree
    be.pan_head(45)
    be.tilt_head(45)
        
    

    rate=rospy.Rate(100)#100hz
    # rospy.spin()
    while not rospy.is_shutdown():
        #rospy.loginfo("Here in the loop")
        be_tree.next()
        rate.sleep()
    #rospy.loginfo("bye")