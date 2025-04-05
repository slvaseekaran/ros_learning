#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool, SetBoolRequest

#initialize node
rospy.init_node('client')

#define my client and wait for service
client = rospy.ServiceProxy('test_service', SetBool)
client.wait_for_service()

#create request message
request = SetBoolRequest()
request.data = True

#receive the response and store it and priny
response = client(request)
print(response)
