ROS:
- Robot Operating System
- Supports modular software design -- NODES

Notes:
- catkin init -- to initilization
- catkin build -- to build your environment

build
- contains build info
- program to machine language

logs
- reports of run exceution

devel
- running nodes (codes)

src
- warehouse of projects


Creating Packages:

Publish and Subscribe
Note: There are many default packages comes along with ros installtion.
command: rospack list

catkin_create_pkg <name>

![](images/Pictures/10000201000002980000005AA02A981BD5EBB9E1.png)

Note:
Good to have codes inside scripts

![](images/Pictures/100002010000019B00000050B5D03FB9A0AA1E71.png)

create python file (code):
![](images/Pictures/10000201000001E40000002E4C50BA877544BBFC.png)

note: permission should be enabled to these newly created files

publisher file:

![](images/Pictures/100002010000028400000141E5CAFAE853AC66EA.png)

publishing topic:

![](images/Pictures/10000201000002990000028442BCFAE09A7481EE.png)

Note:
Add this to avoid sourcing again and again.

![](images/Pictures/1000020100000249000000841A63C7999262818E.png)

Subscriber file:

![](images/Pictures/10000201000003140000014A3DC5EF67BE6B57FD.png)

subscribing topic:

![](images/Pictures/100002010000029A00000256D995D03AEF201069.png)

Note: If we want to delete the packages, direct deletion cannot remove
all related files inside build, devel and logs. We still need to remove
them.

Command: catkin clean --orphans

ROS LAUNCH:

Let's say we have 10 different nodes, how can we run all these nodes at
a particular time, then the ros launch came into action.

Create launch file:

![](images/Pictures/100002010000036D00000088176A95DCB1973F26.png)

running launch file:

![](images/Pictures/1000020100000269000002378C8B0880A843ACA9.png)

note: while running roslaunch, both publisher and subscriber nodes are
running simultaneously

we can feel this on running rosnode list and rostopic list

About RQT Tool:

command: rqt

we can examine relationship between publisher node, subscriber node and
topics.

PLAY with [Turle sim](https://wiki.ros.org/turtlesim), it is really
crazy!!
Turtle sim automatically publisher/subscribe topic (check -- rostopic
info), just we only need to create publisher/subscriber node to publish
topics accordingly.

- just to move turtle in x direction
- just check rostopic echo

![](images/Pictures/100002010000028A00000146B59C2EDFFABDEC1F.png)

![](images/Pictures/10000201000002AE0000020ECD7230F8C143FD33.png)

![](images/Pictures/100002010000054800000294CD2C2D48C15302F5.png)


Client and Server

- client request for service from the server | server is mandatory
- request and response

creating server-client package:

![](images/Pictures/1000020100000236000002110D7A447D48A3AAE5.png)

![](images/Pictures/1000020100000219000001B611151922A4610FAC.png)

![](images/Pictures/100002010000027B00000268A801AF1CDE3F1745.png)

rosservice call <service_name> "date: true/false"

Note: in publish and subscribe -- there is no need for subscriber all
time

search in ros installation for service
computer/opt/ros/noetic/share/std_srvs

we can say ~ msgs are subset of services


ROS Parameter Server:
- associated with roscore
- stores parameter

![](images/Pictures/100002010000029E0000027788EEA72C11FF78AB.png)

Notes:

we cannot do this everytime in terminal. We need this in some automated
scripts
we can only get this running only from roslaunch command
we need to create 'yaml' file -- basically a database

Create -- Ros Param Yaml File

![](images/Pictures/100002010000013000000075B34CCE77EDBD2903.png)

Simillary like, to run many topic at a particular time -- we use ros
launch file.
We need to include this yaml file aslo there in launch file

create -- Launch File (for param (yaml file))

![](images/Pictures/100002010000035A0000008B2E24AACB150F6AA0.png)

running launch file:

![](images/Pictures/10000201000002990000029370225C5899F8BE7D.png)

Here, in launch file, path of config is little tedious (not same for
everyone)

edit like this

![](images/Pictures/10000201000002C00000007E13C5F1F7E0007270.png)

Rosbags:
Bags for storing ros-data

- run roscore
- record rosbag
- publish topic varibales

- play rosbag (where you can see traces)
- rostopic echo and look for traces

![](images/Pictures/10000201000002980000028191E7F81811320D8F.png)

create python file to view bags contents instead of echoing

read_bag file:

![](images/Pictures/100002010000031C0000012E9AB68057BDA50987.png)

output:

![](images/Pictures/10000201000002320000011C0A7FDBA03D2912FB.png)

Quick Collective Works:

publisher:

![](images/Pictures/100002010000029E0000017BC40001BDD92D7EE4.png)

subscriber:

![](images/Pictures/100002010000031E00000167B47D7202D70E3C8E.png)

launch:

![](images/Pictures/100002010000038400000099EA502A3F90B27D49.png)

read bag:

![](images/Pictures/100002010000031B0000023802A0E17C3AA8654D.png)

running roscore:

recording rosbags with all topics:

![](images/Pictures/1000020100000268000001197BD511256DF508B2.png)

running launch file:

![](images/Pictures/10000201000002730000008180B102D84F7734E4.png)

Playing rosbag:

![](images/Pictures/10000201000001E5000002582AA2084BE90965D8.png)
