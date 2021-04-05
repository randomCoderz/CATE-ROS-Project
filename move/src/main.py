#!/usr/bin/env python

import sys
import rospy
from movement import Movement

if __name__ == '__main__':
    move = Movement()
    move.movebot_forward()
    move.movebot_forward()
    move.movebot_forward()
    move.movebot_forward()
    move.movebot_forward()
    rospy.spin()