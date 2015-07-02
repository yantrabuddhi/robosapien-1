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

# This checks if the robot has drifted from the straight path it was supposed to be. Returns true if it is in the path
def checkHeading():
    heading=getCompass()
    # rospy.loginfo("values   %f   %f",heading[0],heading[-1])
    divergence=heading[0]-heading[-1]
    rospy.loginfo('Heading data  %f   %f  ',heading[0],heading[-1])
    rospy.loginfo("this is the divergence %f",divergence)
    if abs(divergence) < compassTolerance:
        # The heading is fine!
        return (True,divergence)   
    return (False,divergence)


def turn_Body():
    # rospy.loginfo("turning body in some direction")
    # heading=getCompass()
    
    # drift=heading[0]-heading[-1]
    value=checkHeading()
    while not value[0]:
        # rospy.loginfo('heading= '+str(heading))
        rospy.loginfo("working on turning on the body")
        # rospy.loginfo('Heading data  %f   %f  ',heading[0],heading[-1])
        if value[1] < 0:
            direction='turn left'
        else:
            direction='turn right'

        robot_cmd_pub.publish(direction,100)
        delay(3)
        value=checkHeading()
        # heading=getCompass() 
        # drift=heading[0]-heading[-1]
        # delay(1.5)   

# This is a function that allows the body to move forward
def moveForward():
    while True:
        topic = rospy.get_param('~topic','/sense/robot/get_compass_deg')
        rospy.Subscriber(topic,compass,readCompass)
        delay(1.5)   
        rospy.loginfo("issue walkf forward command")
        robot_cmd_pub.publish('walk forward',150)
        delay(3)

        if not checkHeading()[0]:
            turn_Body()
        else:   
            rospy.loginfo("Heading is correct, continue to move forward")
    rospy.spin()    
# Stops the movement
def stop_movement():
    if not rospy.is_shutdown():
        clearFlags()
        robot_cmd_pub.publish('stop', 0)


# This is a call back fucntion that gets called when ever we have a gyroscope reading
def readCompass(data):
    # rospy.loginfo("READ COMPASS IS CALLED")

    compass_data["heading"].append(data.heading_deg)
    # moveForward()

# This returns back the reading for the compass data 
def getCompass():
    return compass_data["heading"]



# def readSonarDist(data):
#     sonar_data["distance"] = data.distance_cm
     

# def getSonarDistance():
#     return sonar_data["distance"]


def clearFlag(flag):
    flag[flag]=False
def clearFlags():
    for index in flags:
        flags[index] = False

def raiseFlag(flag):
    flags[flag] = True

def isFlagRaised(flag):
    return flags[flag]

def Test():
    abeni='none'



if __name__ == '__main__':
    try:       
        #Constants
        TOLERANCE = 15
        Error= 2
        Error2=5
        compassTolerance=5
        # Init Node
        rospy.init_node('moveForward', anonymous = False)

        # Init publishers
        # pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 1)
        # tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 1)
        pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 1)
        tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 1)
        robot_cmd_pub = rospy.Publisher('/act/robot/send_move_command', robot_cmd, queue_size = 10)
        
        # Wait for bluetooth to connect
        waitForBT()

        # Init variables
        angles = {"pan" :[45], "tilt" :[45]}
        # sonar_data = {"distance" : 200}
        compass_data={"heading":[]}
        # compassHeading=[0]
        #defines the current state of the robot
        flags = {"turn left" : False, "turn right" : False, "walk forward" : False,"Camera track":False,"Body track":False,"follwing":False}  

        # Move head to default position
        pan_head(45)
        tilt_head(45)
        moveForward()

    except rospy.ROSInterruptException:
        pass
