#!/usr/bin/env python

import sys
import rospy

if __name__ == '__main__':
    rospy.init_node('road_detection', anonymous=True)
    rospy.spin()