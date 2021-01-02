#!/usr/bin/env python
import sys
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

PI = 3.1415926535897
move_topic = '/husky_velocity_controller/cmd_vel'
odometry = '/husky_velocity_coontroller/odom'

# Moves bot forward manually
def movebot_forward():
    pub = rospy.Publisher(move_topic, Twist, queue_size=10)
    rospy.init_node('Movement', anonymous=True)
    rate = rospy.Rate(10)
    vel_msg = Twist()
    while not rospy.is_shutdown():
        vel_msg.linear.x = 10
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        rospy.loginfo("Publishing forward...")
        pub.publish(vel_msg)
        rate.sleep()

# Moves bot right manually
def movebot_right():
    pub = rospy.Publisher(move_topic, Twist, queue_size=10)
    rospy.init_node('Movement', anonymous=True)
    rate = rospy.Rate(10)
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 10
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    rospy.loginfo("Publishing right...")
    pub.publish(vel_msg)
    rate.sleep()

# Moves bot left
def movebot_left():
    pub = rospy.Publisher(move_topic, Twist, queue_size=10)
    rospy.init_node('Movement', anonymous=True)
    rate = rospy.Rate(10)
    vel_msg = Twist()

    while not rospy.is_shutdown():
        vel_msg.linear.x = -10
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        rospy.loginfo("Publishing left...")
        pub.publish(vel_msg)
        rate.sleep()

# Moves bot backwards
def movebot_reverse():
    pub = rospy.Publisher(move_topic, Twist, queue_size=10)
    rospy.init_node('Movement', anonymous=True)
    rate = rospy.Rate(10)
    vel_msg = Twist()

    while not rospy.is_shutdown():
        vel_msg.linear.x = -10
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        rospy.loginfo("Publishing reverse...")
        pub.publish(vel_msg)
        rate.sleep()

# Adapater for Deep learning algorithm
# def movebot_auto(linear_x, linear_y, linear_z, angular_x, angular_y, angular_z):
#     pub = rospy.Publisher(velocity_topic, Twist, queue_size=10)
#     rospy.init_node('Movement', anonymous=True)
#     rate = rospy.Rate(10)
#     vel_msg = Twist()

#     while not rospy.is_shutdown():
#         vel_msg.linear.x = linear_x
#         vel_msg.linear.y = linear_y
#         vel_msg.linear.z = linear_z
#         vel_msg.angular.x = angular_x
#         vel_msg.angular.y = angular_y
#         vel_msg.angular.z = angular_z
#         rospy.loginfo("Publishing...")
#         pub.publish(vel_msg)
#         rate.sleep()


if __name__ == '__main__':
    try:
        movebot_forward()
    except rospy.ROSInterruptException: pass