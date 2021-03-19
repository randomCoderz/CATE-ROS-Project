#!/usr/bin/env python3

import sys
import rospy
from movement import Movement

if __name__ == '__main__':
    move = Movement()
    try:
        move.movebot_forward()
        move.movebot_right()
        move.movebot_left()
        move.movebot_reverse()
    except rospy.ROSInterruptException: pass