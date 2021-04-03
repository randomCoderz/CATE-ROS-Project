#!/usr/bin/env python

import sys
import rospy
from road import Road

if __name__ == '__main__':
    rd = Road()
    rospy.init_node('vision_node', anonymous=True)
    rospy.spin()