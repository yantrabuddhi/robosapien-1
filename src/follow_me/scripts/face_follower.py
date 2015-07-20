#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import Int32
from vision.msg import targets

def waitForBT():
    time.sleep(6)    

def pan_head(angle):    
    if not rospy.is_shutdown():
        pan_angle_pub.publish(angle)

def tilt_head(angle):
    if not rospy.is_shutdown():
        tilt_angle_pub.publish(angle) 

def faceDetected(boxes):
    # Get face bounding box
    face_left = boxes.faces[0].top_left.x
    face_top = boxes.faces[0].top_left.y
    face_width = boxes.faces[0].width_height.x
    face_height = boxes.faces[0].width_height.y

    # Calculate correction
    ideal_left = 0.5 - face_width / 2.0
    correction_pan = (ideal_left - face_left) * 2.5

    ideal_top = 0.5 - face_height / 2.0
    correction_tilt = (ideal_top - face_top) * 2.5

    # print correction
    angles["pan"] += correction_pan
    angles["tilt"] -= correction_tilt

    # Limit pan and tilt angles
    if (angles["pan"] < 0): 
        angles["pan"] = 0
    elif (angles["pan"] > 90):
        angles["pan"] = 90

    if (angles["tilt"] < 0): 
        angles["tilt"] = 0
    elif (angles["tilt"] > 90):
        angles["tilt"] = 90

    # Publish correction
    pan_head(angles["pan"])
    tilt_head(angles["tilt"])


if __name__ == '__main__':
    try:       
        # Init Node
        rospy.init_node('face_follower', anonymous = False)

        # Init publishers
        pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 1)
        tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 1)
        
        # Wait for bluetooth to connect
        waitForBT()

        # Init angles
        angles = {"pan" : 45, "tilt" : 45}
        pan_head(angles["pan"])
        tilt_head(angles["tilt"])

        # Read from facedetect
        rospy.Subscriber('facedetect', targets, faceDetected)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass