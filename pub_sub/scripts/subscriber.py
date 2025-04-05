#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def callback(msg):  #defining the function
    print(msg)

rospy.init_node('subscriber')  #initialize this node
rospy.Subscriber('vel_x', Int64, callback)   #callback function
rospy.Subscriber('vel_y', Int64, callback)
rospy.Subscriber('vel_z', Int64, callback)

#note: subscriber is suppose to run indefinitely untill the ros core is terminated
rospy.spin()  #instead of while loop
