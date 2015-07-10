#!/usr/bin/python
 
#----------------------------------------------------------------------------
# Face Detection Test (OpenCV)
#
# thanks to:
# http://japskua.wordpress.com/2010/08/04/detecting-eyes-with-python-opencv
#----------------------------------------------------------------------------

import cv2
import rospy
import sys
import numpy as np
import os
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from vision.msg import face_box
from vision.msg import targets

from cv_bridge import CvBridge, CvBridgeError

class FaceRecognize:
    NODE_NAME = 'face_recognize'

    def __init__(self):
        self.haarbase = '/usr/share/opencv/' #'/opt/ros/hydro/share/OpenCV/' #'/usr/share/opencv/'
        self.faceCascade = cv2.CascadeClassifier(self.haarbase + "haarcascades/haarcascade_frontalface_alt.xml")
        self.pub = rospy.Publisher('/facerecognize', targets, queue_size=10)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/cv_camera/image_raw",Image,self.callback)

        # Get training data
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.recognizablePeople = self.get_subDirs("faces")
        images = []
        labels = []
        for person in self.recognizablePeople:
            for trainingFile in os.listdir("faces/" + person):
                images.append(cv2.imread("faces/" + person + "/" + trainingFile, cv2.IMREAD_GRAYSCALE))
                labels.append(self.recognizablePeople.index(person))
                print "faces/" + person + "/" + trainingFile, "  ----  ", self.recognizablePeople.index(person)

        # Train recognizer
        self.faceRecognizer = cv2.createFisherFaceRecognizer()
        # faceRecognizer = cv2.createEigenFaceRecognizer()
        print "Beginning Training..."
        self.faceRecognizer.train(np.asarray(images), np.asarray(labels))
        print "Training Over"
        
    def get_subDirs(self, parentDir):
        return [name for name in os.listdir(parentDir)
            if os.path.isdir(os.path.join(parentDir, name))]

    def callback(self,data):
        try:
            source = self.bridge.imgmsg_to_cv2(data,"bgr8")#imgmsg_to_cv2
            # source = np.asarray(source)
            # print "S1 = ", source.shape[1], "S0 = ", source.shape[0]
            # bitmap = cv2.cv.CreateImageHeader((source.shape[1], source.shape[0]), cv2.IPL_DEPTH_8U, 3)
            # bitmap = np.zeros((source.shape[1],source.shape[0],3), np.uint8)
            # cv2.cv.SetData(bitmap, source.tostring(),source.dtype.itemsize * 3 * source.shape[1])
            # cv_image = bitmap
        except CvBridgeError, e:
            print e
            
        #(cols,rows) = cv2.GetSize(cv_image)
        img = self.DetectFace(source, self.faceCascade)
        cv2.imshow("ImageShow", img)    
        cv2.waitKey(10)

#rospy.init_node('face_locations', anonymous=True)
#r = rospy.Rate(10) # 10hz

    def DetectFace(self,image, faceCascade):    
        # Allocate the temporary images
        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(grayscale, 1.3, 5)

        # If faces are found
        if len(faces) > 0:
            payload = targets()
            payload.ref_img_width = image.shape[1]
            payload.ref_img_height = image.shape[0]
            for (x, y, w, h) in faces:
                faceSmall = cv2.resize(grayscale[y:y + h, x:x + w], (150, 150))
                prediction, mismatch = self.faceRecognizer.predict(faceSmall)
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                fbox = face_box()
                fbox.top_left.x=float(x) / float(image.shape[1])
                fbox.top_left.y=float(y) / float(image.shape[0])
                fbox.width_height.x=float(w) / float(image.shape[1])
                fbox.width_height.y=float(h) / float(image.shape[0])
                fbox.name = self.recognizablePeople[prediction]
                fbox.mismatch = mismatch
                payload.faces.append(fbox)

            msg = payload

            rospy.loginfo(msg)
            self.pub.publish(msg)
     
        return image
 
#----------
# M A I N
#----------
def main(args):
    rospy.loginfo("Starting {0}...".format(FaceRecognize.NODE_NAME))

    ic = FaceRecognize()

    rospy.init_node('face_detect', anonymous=False)

    rospy.loginfo("{0} started, listening for image input on topic /cv_camera/image_raw, publishing on topic facerecognize".format(FaceRecognize.NODE_NAME))
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "shutting down"
        rospy.loginfo("Stopping {0}...".format(FaceRecognize.NODE_NAME))
        rospy.loginfo("{0} stopped.".format(FaceRecognize.NODE_NAME))

    cv2.destroyAllWindows()
     
if __name__=='__main__':
    main(sys.argv)
