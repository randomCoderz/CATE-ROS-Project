#!/usr/bin/env python

import sys

import rospy
from image_train import image_capture

if __name__ == '__main__':
    rospy.init_node('vision_node', anonymous=True)
    image_capture()
    rospy.spin()