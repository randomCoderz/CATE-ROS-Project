# Captures data from simulation as images for training
import sys

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_capture:
    
    count = 0
    
    def __init__(self):
        self.bridge = CvBridge()
        self.pub = rospy.Publisher('opencv/road',Image,queue_size=10)
        self.image_sub = rospy.Subscriber("/sensor/camera/image_raw",Image,self.callback)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        
        file_name = '/home/am/Desktop/tensorflow-simulation/image-data/' + 'image_' + str(self.count) + '.png'
        cv2.imwrite(file_name, cv_image)
        self.count += 1
        rospy.sleep(2)
