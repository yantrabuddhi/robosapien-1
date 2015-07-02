#!/usr/bin/env python

import rospy
from utils import clamp, waitForBT
from std_msgs.msg import String
from std_msgs.msg import Int32
from tld_msgs.msg import BoundingBox
from robot.msg import robot_cmd
from robot.msg import sonar

def pan_head(angle):    
    if not rospy.is_shutdown():
        pan_angle_pub.publish(angle)

def tilt_head(angle):
    if not rospy.is_shutdown():
        tilt_angle_pub.publish(angle) 

def move_body(direction):
    if not rospy.is_shutdown():
        if (direction == "left"):
            robot_cmd_pub.publish('left turn step', 0)
        elif (direction == "right"):
            robot_cmd_pub.publish('right turn step', 0)

def move_forward():
    if not rospy.is_shutdown():
        robot_cmd_pub.publish('walk forward', 0)

def readSonarDist(data):
    sonar_data["distance"] = data.distance_cm

def getSonarDistance():
    return sonar_data["distance"]


def objectDetected(tracked_object):
    object_left  = tracked_object.x
    object_top   = tracked_object.y
    object_width = tracked_object.width
    object_height = tracked_object.height   
    
    if object_left > 5 and object_top > 5:
        # Calculate correction
        ideal_left = 320 - object_width / 2.0
        correction_pan = (ideal_left - object_left) / 50.00

        ideal_top = 240 - object_height / 2.0
        correction_tilt = (ideal_top - object_top)/ 50.00

        angles["pan"] += correction_pan
        angles["tilt"] -= correction_tilt

        # Clamp pan and tilt angles
        angles["pan"] = clamp(0, angles["pan"], 90)
        angles["tilt"] = clamp(0, angles["tilt"], 90)

        # Publish new values
        pan_head(angles["pan"])
        tilt_head(angles["tilt"])


    # Move body
    if (angles["pan"] < 40): # Move body to left
        move_body("right")
    elif (angles["pan"] > 50): # Move body to the right
        move_body("left")
    elif (getSonarDistance > 50):
        move_forward()
    


if __name__ == '__main__':
    try:       
        # Init Node
        rospy.init_node('object_follower_body', anonymous = False)

        # Init publishers
        pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 10)
        tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 10)
        robot_cmd_pub = rospy.Publisher('/act/robot/send_move_command', robot_cmd, queue_size = 10)

        # Wait for bluetooth to connect
        waitForBT()

        # Init angles
        angles = {"pan" : 45, "tilt" : 45}
        sonar_data = {"distance" : 200}
        
        pan_head(angles["pan"])
        tilt_head(angles["tilt"])

        # Read from tld_tracked_object
        rospy.Subscriber('tld_tracked_object', BoundingBox, objectDetected)
        rospy.Subscriber('/sense/robot/get_sonar_cm', sonar, readSonarDist)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass