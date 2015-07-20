#!/usr/bin/env python
import owyl
from owyl import blackboard
import rospy
import numpy as np
from utils import clamp, waitForBT,delay
from std_msgs.msg import String
from std_msgs.msg import Int32
from robot.msg import robot_cmd
from robot.msg import sonar
from robot.msg import compass
from geometry_msgs.msg import Point


class behavior:
    def __init__(self,bb):
        self.blackboard=bb#blackboard.Blackboard("behavior")
        #rospy.loginfo (self.blackboard["stt"])
        self.main_tree=self.create_main_tree()
       
        self.Error2=5
        self.cameraSettleTolerance=50
        self.bodySettleTolerance=2
        
        # This two are used for searching ball when the ball is not found;  (search function)
        # self.prevPanLen holds the lenght of the panAngle list before searching is performed
        self.prevPanLen=1
        # self.currentpanLen holds the current lenght of the panAngle list after searching is performed
        # It the two are different we can infer that the ball has been spotted during searching and search was success
        self.currentPanLen=1
        self.scanning_tilt=80
        
    def create_main_tree(self):
        # tree=owyl.repeatAlways(self.isCameraTrack())
        tree=owyl.repeatAlways(
                owyl.sequence(
                    owyl.selector(self.checkIfBall(),owyl.selector(self.search80(),self.search55(),search30(),self.turnBody()))
                    ,owyl.repeatUntilSucceed(self.isCameraTrack())
                    ,owyl.repeatUntilSucceed(self.isBodyTrack())
                    ,self.isWalkForward()
                    )
                )
         
        # tree=owyl.repeatAlways(self.isCameraTrack())
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
    def checkIfBall(self,**kwargs):
        # rospy.loginfo("checking if ball exists")
        delay(2)
        if len(self.blackboard["angles"]["pan"])>30:
            # ball is already detected. Jump to camera mode
            # self.CT()
            self.reintialize()
            yield True
        else:
            self.reintialize()
            yield False
    @owyl.taskmethod
    def search80(self,**kwargs):
        # rospy.loginfo("at 80 search")
        self.scanning_tilt=80
        self.pan_head(0)
        delay(1)
        self.tilt_head(self.scanning_tilt)
        delay(1)
        # Next turn the body smoothly from right to left at a step of 5 degrees for a total of 90 degrees
        for i in range (10,95,10):
            self.pan_head(i)
            delay(0.5)
            # check if a ball was spotted every multiple of 10 degree angle
            if i%10==0:
                self.currentPanLen=len(self.blackboard["angles"]["pan"])
                # rospy.loginfo("current  %f ,  prev  %f",self.currentPanLen,self.prevPanLen)
                if self.currentPanLen > self.prevPanLen+10:
                    # a ball was spotted (pan angle has been appended by the call back function)
                    # so break the loop and yield True
                    break
        
        if i <= 85:
            rospy.loginfo("got it")
            # rospy.loginfo("before current pan angles %f  ",self.blackboard["angles"]["pan"][-1])
            self.blackboard["angles"]["pan"]=[i]
            self.blackboard["angles"]["tilt"]=[self.scanning_tilt]
            # rospy.loginfo("After current pan angles %f  ",self.blackboard["angles"]["pan"][-1])
            yield True
        else:
            self.reintialize()
            yield False

        
    @owyl.taskmethod
    def search55(self,**kwargs):
        rospy.loginfo("at 60 search")
        self.scanning_tilt=55
        self.pan_head(0);
        delay(1)
        self.tilt_head(self.scanning_tilt);
        delay(1)
        # Next turn the body smoothly from right to left at a step of 5 degrees for a total of 90 degrees
        for i in range (10,95,10):
            self.pan_head(i)
            delay(0.5)
            # check if a ball was spotted every 10 multiple degree angle
            if i%10==0:
                self.currentPanLen=len(self.blackboard["angles"]["pan"])
                # rospy.loginfo("current  %f ,  prev  %f",self.currentPanLen,self.prevPanLen)
                if self.currentPanLen > self.prevPanLen+10:
                    # a ball was spotted (pan angle has been appended by the call back function)
                    # so break the loop and yield True
                    break
        
        if i <= 85:
            # rospy.loginfo("got it")
            # rospy.loginfo("before current pan angles %f  ",self.blackboard["angles"]["pan"][-1])
            self.blackboard["angles"]["pan"]=[i]
            self.blackboard["angles"]["tilt"]=[self.scanning_tilt]
            # rospy.loginfo("After current pan angles %f  ",self.blackboard["angles"]["pan"][-1])
            yield True
        else:
            self.reintialize()
            yield False
    @owyl.taskmethod
    def search30(self,**kwargs):
        rospy.loginfo("at 60 search")
        self.scanning_tilt=30
        self.pan_head(0);
        delay(1)
        self.tilt_head(self.scanning_tilt);
        delay(1)
        # Next turn the body smoothly from right to left at a step of 5 degrees for a total of 90 degrees
        for i in range (10,95,10):
            self.pan_head(i)
            delay(0.5)
            # check if a ball was spotted every 10 multiple degree angle
            if i%10==0:
                self.currentPanLen=len(self.blackboard["angles"]["pan"])
                # rospy.loginfo("current  %f ,  prev  %f",self.currentPanLen,self.prevPanLen)
                if self.currentPanLen > self.prevPanLen+10:
                    # a ball was spotted (pan angle has been appended by the call back function)
                    # so break the loop and yield True
                    break
        
        if i <= 85:
            # rospy.loginfo("got it")
            # rospy.loginfo("before current pan angles %f  ",self.blackboard["angles"]["pan"][-1])
            self.blackboard["angles"]["pan"]=[i]
            self.blackboard["angles"]["tilt"]=[self.scanning_tilt]
            # rospy.loginfo("After current pan angles %f  ",self.blackboard["angles"]["pan"][-1])
            yield True
        else:
            self.reintialize()
            yield False

    @owyl.taskmethod
    def turnBody(self,**kwargs):
        rospy.loginfo("at turn body search")
        self.CT()
        for i in range(3):
            self.blackboard["robot_cmd_pub"].publish('turn left',250)
            if len(self.blackboard["angles"]["pan"])>10:
                break
            delay(4)
        if i<2:
            yield True
        else:
            self.reintialize()
            yield False

    @owyl.taskmethod
    def isCameraTrack(self,**kwargs):
        rospy.loginfo("I'm in camera track mode")
        self.CTDone=False
        self.PrevPandata=len(self.blackboard["angles"]["pan"])
        while not self.CTDone:
            if len(self.blackboard["angles"]["pan"])<self.cameraSettleTolerance:
                # not enough data yet to decide wheter camera has settled or not!
                #rospy.loginfo("current pan angles %f  ",self.blackboard["angles"]["pan"][-1])
                self.CT()
                self.currPanData=len(self.blackboard["angles"]["pan"])

                yield False
            else:
                #rospy.loginfo("In else stat")
                self.Mean=np.mean(self.blackboard["angles"]["pan"][-10:-1])
                # rospy.loginfo("This is the mean" + str(Mean))
                self.check1=(self.blackboard["angles"]["pan"][-1]) + self.Error2
                self.check2=(self.blackboard["angles"]["pan"][-1]) - self.Error2
                # check if pan angles has settled (in effect camera track has settled)
                if self.Mean<=self.check1 and self.Mean>=self.check2:
                    # clearFlags()
                    #record heading degrees right after the end of camera tracking
                    self.blackboard["bodyPose"].append(self.blackboard["angles"]["pan"][-1]-45)
                    self.blackboard["HeadingAfterCT"].append(self.getCompass()[-1])
                    #Camera Track done!
                    rospy.loginfo("Done with CT")
                    self.CTDone=True
                    yield True
                else:
                    self.CT()
                    yield False
            
        # '''
        ##  Testing code for camera tracker!
        # while True:
        #     rospy.loginfo("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        #     self.CT()
        #     yield False
        # # '''
    @owyl.taskmethod
    def isBodyTrack(self, **kwargs):
        rospy.loginfo("I'm in Body Track mode")
        bodyPose=self.blackboard["bodyPose"][0]
        heading=self.getCompass()
        self.BTDone=False
        # bodyToGo=heading[-1]-self.getHeadingCT()
        while not self.BTDone:
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
                delay(2.0)
                self.BTDone=True
                yield True
    @owyl.taskmethod
    def isWalkForward(self, **kwargs):
        self.pan_head(self.blackboard["start_pan"])
        delay(0.2)
        self.tilt_head(self.blackboard["start_tilt"])
        delay(0.2)
        self.blackboard["robot_cmd_pub"].publish('walk forward',250)
        delay(3.0)
        self.reintialize()
        yield True


    # return all values to default to restart the whole process of tracking again   
    def reintialize(self):
        # self.blackboard["angles"] = {"pan" :[self.blackboard["angles"]["pan"][-1]], "tilt" :[self.blackboard["angles"]["tilt"][-1]]}
        self.blackboard["angles"] = {"pan" :[self.blackboard["start_pan"]], "tilt" :[self.blackboard["start_tilt"]]}
        self.blackboard["sonar_data"] = {"distance" : [200]}
        self.blackboard["compass_data"]={"heading":[]}
        self.blackboard["bodyPose"]=[]
        self.blackboard["HeadingAfterCT"]=[]
        self.prevPanLen=1
        self.currentPanLen=1


    def CT(self):
        '''
            This function publishes to the camera servo motors publishers  i.e /act/robot/set_pan_angle and /act/robot/set_tilt_angle
            Publishes the last pan and tilt angles from the pan and tilt lists
        '''

        #rospy.loginfo("CALLED")
        # rospy.loginfo("pan %f  , tilt %f  ",self.blackboard["angles"]["pan"][-1],self.blackboard["angles"]["tilt"][-1])
        self.tilt_head(self.blackboard["angles"]["tilt"][-1])
        delay(0.1)
        self.pan_head(self.blackboard["angles"]["pan"][-1])
        delay(0.1)


    def pan_head(self,angle):    
        '''
            A publisher function to the pan servo

            arguments (angle in degree. Should be  0-90, otherwise it will be clipped to 0 or 90)
        '''
        if not rospy.is_shutdown():
            self.blackboard["pan_angle_pub"].publish(angle)

    def tilt_head(self,angle):
        '''
            A publisher function to the tilt servo motors

            arguments (angle in degree. should be 0-90, otherwise it will be clippped to 0 or 90)
        '''
        if not rospy.is_shutdown():
            self.blackboard["tilt_angle_pub"].publish(angle) 

    def stop_movement():
        '''
           A publihser function to the robot.  It will stop any command send to the robot.   
              publishes to /act/robot/send_move_command

        '''
        if not rospy.is_shutdown():
            self.blackboard["robot_cmd_pub"].publish('stop', 0)

    
    def getSonarDistance(self):
        '''
           Function to access the list of sonar readings
        '''
        return self.blackboard["sonar_data"]["distance"]


    def getCompass(self):
        '''
           Function to access the list of compass reading
        '''
        return self.blackboard["compass_data"]["heading"]

    def getHeadingCT(self):
        '''
            Function to access the first reading of the compass right after the camera has settled on tracking the object
            This heading value is used to calculate (with the help of the current camera pan angle) how much the body needs
            turn.

            Used by the bodyTrack node of the owyl behavior tree.


            returns :  the compass reading right after the camera track has settled
        '''
        return self.blackboard["HeadingAfterCT"][0]




def faceDetected(points):
    '''
    This is the callback function that is called when ever a ball is detected!
    It performs the PD controller task required to track the ball
    

    Inputs =>  geometry_msgs.points==>  points is a pair of (x,y) that is the top_left corner of the tracked ball
    
    output:
        It directly writes to the angles dictionary that is a dictionary of list of pan and tilt angles indepedently
        It Performs PD controller on the pan and tilt command then append it to the dictionary so that any function 
        interested can use them to publish the values.

    '''

    # grab the top left corner as x-axis
    x=points.x
    # gradthe top left corner as y-axis
    y=points.y

    # Ideally the point should be at the center of the camera view (i.e (x,y)= (0.5,0.5))
    ideal_left = 0.5
    ideal_top  = 0.5 
    
    # Find the derivative terms
    dx=(x-x_prev)/dt
    dy=(y-y_prev)/dt


    # Find the control signal using PD controller
    correction_pan = k*(ideal_left - x)-kdx*(dx) 
    correction_tilt= k*(ideal_top - y)-kdy*(dy)

    # prepare for clamping the values
    temp1=board["angles"]["pan"][-1] + correction_pan
    temp2=board["angles"]["tilt"][-1]- correction_tilt

    # rospy.loginfo("This is pan and tilt correction %f   %f :  ",correction_pan, correction_tilt)
    # Clamp pan and tilt angles
    board["angles"]["pan"].append(clamp(0, temp1, 90))
    board["angles"]["tilt"].append(clamp(0, temp2, 90))




def readSonarDist(data):
    board["sonar_data"]["distance"].append(data.distance_cm)

def readCompass(data):
    board["compass_data"]["heading"].append(data.heading_deg)
    
    

    

if __name__=="__main__":
    # Initialize Node
    rospy.init_node('behavior', anonymous = False)
    
    # Initialize Publishers
    pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 1)
    tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 1)
    robot_cmd_pub = rospy.Publisher('/act/robot/send_move_command', robot_cmd, queue_size = 1)
    
    # Initialize subscribers
    rospy.Subscriber('/ball_pose',Point, faceDetected)
    rospy.Subscriber('/sense/robot/get_sonar_cm', sonar, readSonarDist)
    rospy.Subscriber('/sense/robot/get_compass_deg',compass,readCompass)
    


    # create an object of black board 
    board=blackboard.Blackboard()
    
    # publishers on board
    board["pan_angle_pub"]  = pan_angle_pub
    board["tilt_angle_pub"] = tilt_angle_pub
    board["robot_cmd_pub"]  = robot_cmd_pub
    
    # Init variables
    board["angles"] = {"pan" :[45], "tilt" :[60]}
    board["sonar_data"] = {"distance" : [200]}
    board["compass_data"]={"heading":[0]}
    board["bodyPose"]=[]
    board["start_pan"]=45
    board["start_tilt"]=60
    board["HeadingAfterCT"]=[] # This records the heading right after the camera track has stopped
    board["scanning tilt"]=80  # This initializes the first tilt for scanning using search function



    TOLERANCE = 15
    Error= 2
    Error2=5

    # Initialize terms for PD controllers
    x_prev=board["start_pan"]   # previous x-pos
    y_prev=board["start_tilt"]   # previous y-Pos
    k=3.5       # constant of linear term
    kdx=0.0005      # differential pan gain 
    kdy=0.00000     # differential tilt gain
    dt=0.1     # rate of time between call back ... I guessed this one


    # Create a behavior tree using the blackboard object board
    be=behavior(board)

    # call to the main tree (root)
    be_tree=be.main_tree
    
    
    # Wait for bluetooth to connect
    waitForBT()

    # Move head to default position
    be.pan_head(board["start_pan"])
    be.tilt_head(board["start_tilt"])
        
    

    rate=rospy.Rate(100)#100hz
    # rospy.spin()
    while not rospy.is_shutdown():
        #rospy.loginfo("Here in the loop")
        be_tree.next()
        rate.sleep()
    #rospy.loginfo("bye")