#!/usr/bin/env python3 

import rospy  #ros to run pyhton code
from std_msgs.msg import Int64

rospy.init_node('publisher_node')  #initialize this node
pub1 = rospy.Publisher('vel_x', Int64, queue_size= 1)
pub2 = rospy.Publisher('vel_y', Int64, queue_size= 1)
pub3 = rospy.Publisher('vel_z', Int64, queue_size= 1)

# Looping
while not rospy.is_shutdown(): #untill it should run
    pub1.publish(1)
    pub2.publish(2)
    pub3.publish(3)
    rospy.sleep(1)
