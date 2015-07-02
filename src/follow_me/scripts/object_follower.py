#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import Int32
# from vision.msg import targets
from tld_msgs.msg import BoundingBox

def waitForBT():
    time.sleep(6)    

def pan_head(angle):    
    if not rospy.is_shutdown():
        pan_angle_pub.publish(angle)

def tilt_head(angle):
    if not rospy.is_shutdown():
        tilt_angle_pub.publish(angle) 

def objectDetected(tracked_object):
    object_left  = tracked_object.x
    object_top   = tracked_object.y
    object_width = tracked_object.width
    object_height = tracked_object.height   
    
    if object_left>5 and object_top>5:
        # # Calculate correction
        ideal_left = 320 - object_width / 2.0
        correction_pan = (ideal_left - object_left) / 50.00

        ideal_top = 240 - object_height / 2.0
        correction_tilt = (ideal_top - object_top)/ 50.00

        # # print correction
        angles["pan"] += correction_pan
        angles["tilt"] -= correction_tilt

        if angles["pan"]<0:
            angles["pan"]=0
        elif angles["pan"]>90:
            angles["pan"]=90
        if angles["tilt"]<0:
            angles["tilt"]=0
        elif angles["tilt"]>90:
            angles["tilt"]=90

        # # Publish correction
        pan_head(angles["pan"])
        tilt_head(angles["tilt"])
    


if __name__ == '__main__':
    try:       
        # Init Node
        rospy.init_node('object_follower', anonymous = False)

        # Init publishers
        pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 1)
        tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 1)
        
        # Wait for bluetooth to connect
        waitForBT()

        # Init angles
        angles = {"pan" : 45, "tilt" : 45}
        pan_head(angles["pan"])
        tilt_head(angles["tilt"])

        # Read from tld_tracked_object
        rospy.Subscriber('tld_tracked_object', BoundingBox, objectDetected)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass