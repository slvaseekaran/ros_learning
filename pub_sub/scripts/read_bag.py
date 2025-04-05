#!/usr/bin/env python3

import rospy
import rosbag

rospy.init_node('read_bag')
bag = rosbag.Bag('/home/vasee/catkin_ws/src/ros_learning/pub_sub/bag/test.bag')

for topic, msg, t in bag.read_messages(topics = ['/vel_x', '/vel_y', '/vel_z']):
    if topic == '/vel_x': 
        print('vel-x')
        print(msg)
        print('time:', t)
        print('')

    if topic == '/vel_y':
        print('vel-y') 
        print(msg)
        print('time:', t)
        print('')

    if topic == '/vel_z': 
        print('vel-z') 
        print(msg)
        print('time:', t)
        print('')
