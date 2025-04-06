#!/usr/bin/env python3

import rospy
import actionlib #server sending msgs(goal) to some movebase packages
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

#callback
def active_cb(extra):
    rospy.loginfo('Goal pose being processed')

def feedback_cb(feedback):
    rospy.login.info('Current Location: '+str(feedback))

def done_cb(status, result):
    if status ==3:
        rospy.loginfo('Goal reached')
    if status ==2 or status == 8:
        rospy.loginfo('Goal cancelled')
    if status == 4:
        rospy.loginfo('Goal aborted')

#initialize node
rospy.init_node('goal_pose')

#create client node
navclient = actionlib.SimpleActionClient('move_base', MoveBaseAction) #SimpleActionClient is some package
navclient.wait_for_server()

# example of navigation goal
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map'
goal.target_pose.header.stamp = rospy.Time.now()

#drafting goal pose
goal.target_pose.pose.position.x = -2.00
goal.target_pose.pose.position.y = 0.750
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.z = 0.660
goal.target_pose.pose.orientation.w = 0.750

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finished = navclient.wait_for_result()

if not finished:
    rospy.logerr('Action server not available')
else:
    rospy.loginfo(navclient.get_result())
