#!/usr/bin/env python

import rospy
import numpy as np
from utils import clamp, waitForBT,delay
from std_msgs.msg import String
from std_msgs.msg import Int32
from vision.msg import targets
from robot.msg import robot_cmd
from robot.msg import sonar
from robot.msg import compass

def pan_head(angle):    
    if not rospy.is_shutdown():
        pan_angle_pub.publish(angle)

def tilt_head(angle):
    if not rospy.is_shutdown():
        tilt_angle_pub.publish(angle) 

def turn_body(direction):
    if not rospy.is_shutdown():
        rospy.loginfo("I'm in the turn-body node")
        rospy.loginfo("Turning the body in this direction ::: %s",direction)

        bodyToGo=compassHeading[-1]-compassHeading[1]
        bodyDirection=angles["pan"][-1]-45
        while(bodyToGo<abs(bodyDirection)-Error):    
            rospy.loginfo("this is the value of body to go and body Direction %f %f",bodyToGo,bodyDirection)
            rospy.loginfo("Turning the body in this direction ::: %s",direction)
            if (direction == "left"):
                clearFlags()
            
                robot_cmd_pub.publish('turn left',150)
                delay(3)
            elif (direction == "right"):
                clearFlags()
            
                robot_cmd_pub.publish('turn right',150)
                delay(3)
            compassHeading.append(getCompass())
            bodyToGo=compassHeading[-1]-compassHeading[1]
            bodyDirection=angles["pan"][-1]-45
        pan_head(45)
        delay(2)    
        stop_movement()
        clearFlags()
        raiseFlag("walk forward")
        walk_forward()
def walk_forward():
    if not rospy.is_shutdown() and isFlagRaised("walk forward"):
        dis=201
        while(dis>8):
            rospy.loginfo("issue walkf forward command")
            robot_cmd_pub.publish('walk forward',250)
            delay(3)
            clearFlags()
            #raiseFlag("Body track")
            #rospy.loginfo("issue body track command")
            bodyFollower()
            dis=getSonarDistance()
        stop_movement()
def stop_movement():
    if not rospy.is_shutdown():
        clearFlags()
        robot_cmd_pub.publish('stop', 0)


def readSonarDist(data):
    sonar_data["distance"] = data.distance_cm
     

def getSonarDistance():
    return sonar_data["distance"]

def readCompass(data):
    compass_data["heading"]=data.heading_deg
    
    
def getCompass():
    return compass_data["heading"]
def turn_Body():
    rospy.loginfo("turning body in some direction")
    heading=getCompass()
    rospy.loginfo('heading= '+str(heading))
    drift=heading[0]-heading[-1]
    while abs(drift)>compassTolerance:
        rospy.loginfo("working on turning on the body")
        if drift < 0:
            direction='turn left'
        else:
            direction='turn right'

        robot_cmd_pub.publish(direction,100)

        delay(1.5)
        heading=getCompass() 
        drift=heading[0]-heading[-1]
        delay(1)   

def checkHeading():
    heading=getCompass()
    # rospy.loginfo("values   %f   %f",heading[0],heading[-1])
    divergence=heading[0]-heading[-1]
    rospy.loginfo("this is the divergence %f",divergence)
    if abs(divergence) < compassTolerance:
        # The heading is fine!
        return True   
    return False

    
def bodyFollower():
    if isFlagRaised("Body track"):    
        rospy.loginfo("*************************I am in the body track mode")
        #rospy.loginfo()

        bodyDirection=angles["pan"][-1]-45
        direction="left" 
        bodyToGo=compassHeading[-1]-compassHeading[1]
        rospy.loginfo("body needs to go this muuuuuuchhhhhh %f",bodyToGo)
        if bodyToGo> abs(bodyDirection)-Error:
            clearFlags()
            stop_movement()
        else:   
            rospy.loginfo("initial compass reading %f",compassHeading[1])
            rospy.loginfo("current compass reading %f",compassHeading[-1])
            rospy.loginfo("Body needs to move %f", bodyDirection)
            if bodyDirection>0:
                raiseFlag("turn left")
                direction="left"
            else:
                raiseFlag("turn right")
                direction="right"
            
            rospy.loginfo("Issue a command to turn the body")
            turn_body(direction)


def clearFlag(flag):
    flag[flag]=False
def clearFlags():
    for index in flags:
        flags[index] = False

def raiseFlag(flag):
    flags[flag] = True

def isFlagRaised(flag):
    return flags[flag]

def evaluate(name):
    rospy.loginfo("*********HERE I'm CALLED To evALUTATE")
    # rospy.loginfo(angles["pan"])
    if name=="faceDetected":
        if len(angles["pan"]) < 100:
            clearFlags()
            raiseFlag("Camera track")
        else:
            # rospy.loginfo("I'm in here to set the body flag")
            Mean=np.mean(angles["pan"][-5:-1])
            # rospy.loginfo("This is the mean" + str(Mean))
            check1=(angles["pan"][-1]) + Error2
            check2=(angles["pan"][-1]) - Error2
            if Mean<=check1 and Mean>=check2:
                clearFlags()
                #record heading degrees right after the end of camera tracking
                compassHeading.append(getCompass())
                raiseFlag("Body track")
                bodyFollower()
                # rospy.loginfo("body flag to be raised" + str(flags))
            else:
                clearFlags()
                raiseFlag("Camera track")
    # if name=="readCompass" and len(compassHeading)>1:
    #     raiseFlag("Body track")
def faceDetected(boxes):
    evaluate("faceDetected")
    if isFlagRaised("Camera track") and not isFlagRaised("Body track"):
        face_left = boxes.faces[0].top_left.x
        face_top = boxes.faces[0].top_left.y
        face_width = boxes.faces[0].width_height.x
        face_height = boxes.faces[0].width_height.y

        # Calculate correction
        ideal_left = 0.5 - face_width / 2.0
        correction_pan = (ideal_left - face_left) * 2.5

        ideal_top = 0.5 - face_height / 2.0
        correction_tilt = (ideal_top - face_top) * 2.5

        temp1=angles["pan"][-1] + correction_pan
        temp2=angles["tilt"][-1]- correction_tilt

        # Clamp pan and tilt angles
        angles["pan"].append(clamp(0, temp1, 90))
        angles["tilt"].append(clamp(0, temp2, 90))

        # Publish new_angles
        pan_head(angles["pan"][-1])
        tilt_head(angles["tilt"][-1])
        clearFlags()
   
    


if __name__ == '__main__':
    try:       
        #Constants
        TOLERANCE = 15
        Error= 2
        Error2=5
        # Init Node
        rospy.init_node('face_follower_body', anonymous = False)

        # Init publishers
        pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 1)
        tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 1)
        robot_cmd_pub = rospy.Publisher('/act/robot/send_move_command', robot_cmd, queue_size = 10)
        
        # Wait for bluetooth to connect
        waitForBT()

        # Init variables
        angles = {"pan" :[45], "tilt" :[45]}
        sonar_data = {"distance" : 200}
        compass_data={"heading":0}
        compassHeading=[0]
        #defines the current state of the robot
        flags = {"turn left" : False, "turn right" : False, "walk forward" : False,"Camera track":False,"Body track":False,"follwing":False}  

        # Move head to default position
        pan_head(45)
        tilt_head(45)
        

        # Read from facedetect
        
        rospy.Subscriber('facedetect', targets, faceDetected)
        rospy.Subscriber('/sense/robot/get_sonar_cm', sonar, readSonarDist)
        rospy.Subscriber('/sense/robot/get_compass_deg',compass,readCompass)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
