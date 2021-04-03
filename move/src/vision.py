#!/usr/bin/env python

import sys

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
class Vision:
    
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/sensor/camera/image_raw",Image,self.callback)
    
    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, encoding="bgr8")
        except CvBridgeError as e:
            print(e)
        