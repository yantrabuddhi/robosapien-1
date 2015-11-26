#!/usr/bin/env python
__author__ = 'mandeep'

#initialize camera position
#state machine
#subscribe to ball position
#if ball not found scan
#if ball found keep centered and keep last seen position error
import rospy
import time
from std_msgs.msg import Int32
from robot.msg import robot_cmd
from geometry_msgs.msg import Point

# Initialize Publishers
pan_angle_pub = rospy.Publisher('/act/robot/set_pan_angle', Int32, queue_size = 1)
tilt_angle_pub = rospy.Publisher('/act/robot/set_tilt_angle', Int32, queue_size = 1)
robot_cmd_pub = rospy.Publisher('/act/robot/send_move_command', robot_cmd, queue_size = 1)

LastPos=Point()
LastCamX=0
LastCamY=0
pan_min=30
pan_max=70
pan_step=5
tilt_min=25
tilt_max=60
tilt_step=5#centering
ball=False
curr_tilt_step=-5#searching
curr_pan_step=-pan_step
scan_count=0

def init_pan():
    global LastCamX
    LastCamX=45
    pan_angle_pub.publish(45)#center
def init_tilt():
    global LastCamY
    LastCamY=60
    tilt_angle_pub.publish(60)#max

def init_cam():
    init_pan()
    init_tilt()

def do_pan_step():
    global LastCamX,curr_pan_step
    a=LastCamX+curr_pan_step
    pan_angle_pub.publish(a)
    LastCamX=a

def do_tilt_step():
    global LastCamY,curr_tilt_step
    a=LastCamY+curr_tilt_step
    tilt_angle_pub.publish(a)
    LastCamY=a


def searchTurnLeft():
    init_cam()
    cmd=robot_cmd('turn left',200)
    robot_cmd_pub.publish(cmd)

def scan():
    global LastCamX, LastCamY, curr_pan_step,curr_tilt_step,scan_count, tilt_max, tilt_min
    if (curr_tilt_step>0 and LastCamY+curr_tilt_step<tilt_max) or (curr_tilt_step<0 and LastCamY+curr_tilt_step>tilt_min):
        if (curr_pan_step>0 and LastCamX+curr_pan_step<pan_max) or (curr_pan_step<0 and LastCamX+curr_pan_step>pan_min):
            do_pan_step()
        else:
            curr_pan_step=curr_pan_step*(-1)
            do_pan_step()
            do_tilt_step()
    else:
        curr_tilt_step=curr_tilt_step*(-1)
        do_tilt_step()
        scan_count=scan_count+1
        if scan_count>1:
            scan_count=0
            searchTurnLeft()


def clamp(l,v,u):
    if (v<l): return l
    if (v>u): return u
    return  v

def centerCam():
    #lastpos
    global LastCamX,LastCamY,LastPos,pan_min,pan_max,tilt_min,tilt_max
    #rospy.loginfo("x: "+str(LastCamX)+" ,y: "+str(LastCamY)+ " ,lx="+str(LastPos.x)+" ,ly="+str(LastPos.y))

    cPosx=int(clamp(pan_min,((1.0-LastPos.x)*0.9)*(pan_max-pan_min)+pan_min,pan_max))#1.0-x
    LastCamX=cPosx
    pan_angle_pub.publish(LastCamX)
    cPosy=int(clamp(tilt_min,((1.0-LastPos.y)*0.6)*(tilt_max-tilt_min)+tilt_min,tilt_max))
    LastCamY=cPosy
    tilt_angle_pub.publish(LastCamY)
    #rospy.loginfo("x: "+str(cPosx)+" ,y: "+str(cPosy)+ " ,lx="+str(LastPos.x)+" ,ly="+str(LastPos.y))



def correctLeft(er):
    #map er to time 1 to 200
    factor=50.0
    cmd=robot_cmd('turn left',clamp(10,(float(er)/factor)*199+1,200))
    robot_cmd_pub.publish(cmd)

def correctRight(er):
    #map er to time 1 to 200
    factor=50.0
    cmd=robot_cmd('turn right',clamp(10,(float(er)/factor)*199+1,200))
    robot_cmd_pub.publish(cmd)

def move_forward(er):
    factor=tilt_max-tilt_min
    #cmd=robot_cmd('walk forward',(float(er)/factor)*199+1)
    #cmd=robot_cmd('walk forward',clamp(10,(float(er)/float(factor))*199+1,200))
    cmd=robot_cmd('walk forward',clamp(10,200,200))
    robot_cmd_pub.publish(cmd)
    #print ((float(er)/float(factor))*199+1)

def tilt_down():
    global LastCamY
    lStep=tilt_step
    LastCamY=clamp(tilt_min,LastCamY-lStep,LastCamY)
    tilt_angle_pub.publish(LastCamY)

def centerBody():
    #center the camera onto the ball
    #if pan not center: turn body and #center pan
    #if tilt not minimum:move forward and #lower tilt
    if not((LastCamX<45+pan_step)and(LastCamX>45-pan_step)):
        if LastCamX<45:#use difference error
            correctRight(45-LastCamX)#swap name if wrong to right
        else:
            correctLeft(LastCamX-45)#swap if wrong
        time.sleep(1)
        init_pan()
        time.sleep(1)

    if (LastCamY>tilt_min):
        move_forward(LastCamY-tilt_min)
        time.sleep(1)
        tilt_down()

def ballDetected(points):
    global LastPos,ball
    if (points.z>-1.0):
        ball=True
        LastPos=points
    else:
        ball=False

if __name__=="__main__":
    # Initialize Node
    rospy.init_node('behavior', anonymous = False)

    init_cam()

    # Initialize subscribers
    rospy.Subscriber('/ball_pose',Point, ballDetected)

    rate=rospy.Rate(1)
    while (not rospy.is_shutdown()):
        if ball:
            centerCam()
            time.sleep(1)
            centerBody()#and move ..center pan, minimize tilt
            time.sleep(1)
        else:
            scan()
        rate.sleep()
