#!/usr/bin/env python

import sys
import rospy
from movement import Movement
from vision import Vision

if __name__ == '__main__':
    ic = Vision()
    rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
    #move = Movement()
    # try:
    #     move.movebot_forward()
    # except rospy.ROSInterruptException: 
    #     pass