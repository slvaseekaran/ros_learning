ROS:\
\
- Robot Operating System

\- Supports modular software design -- NODES

Notes:

\- catkin init -- to initilization

\- catkin build -- to build your environment

build

\- contains build info

\- program to machine language

logs

\- reports of run exceution

devel

\- running nodes (codes)

src

\- warehouse of projects

Creating Packages:

Publish and Subscribe

Note: There are many default packages comes along with ros installtion.

command: rospack list

catkin\_create\_pkg \<name\>

![](images/Pictures/10000201000002980000005AA02A981BD5EBB9E1.png){width="13.795cm"
height="1.87cm"}

Note:\
Good to have codes inside scripts

![](images/Pictures/100002010000019B00000050B5D03FB9A0AA1E71.png){width="9.012cm"
height="1.755cm"}

create python file (code):\
![](images/Pictures/10000201000001E40000002E4C50BA877544BBFC.png){width="11.751cm"
height="1.117cm"}\

note: permission should be enabled to these newly created files

publisher file:

![](images/Pictures/100002010000028400000141E5CAFAE853AC66EA.png){width="11.164cm"
height="5.565cm"}

publishing topic:

![](images/Pictures/10000201000002990000028442BCFAE09A7481EE.png){width="13.176cm"
height="12.76cm"}

Note:\
Add this to avoid sourcing again and again.\

![](images/Pictures/1000020100000249000000841A63C7999262818E.png){width="13.568cm"
height="2.618cm"}

Subscriber file:

![](images/Pictures/10000201000003140000014A3DC5EF67BE6B57FD.png){width="13.481cm"
height="5.646cm"}

subscribing topic:

![](images/Pictures/100002010000029A00000256D995D03AEF201069.png){width="12.568cm"
height="11.284cm"}

Note: If we want to delete the packages, direct deletion cannot remove
all related files inside build, devel and logs. We still need to remove
them.

Command: catkin clean --orphans

ROS LAUNCH:

Let's say we have 10 different nodes, how can we run all these nodes at
a particular time, then the ros launch came into action.

Create launch file:

![](images/Pictures/100002010000036D00000088176A95DCB1973F26.png){width="12.282cm"
height="1.905cm"}

running launch file:

![](images/Pictures/1000020100000269000002378C8B0880A843ACA9.png){width="15.49cm"
height="14.235cm"}

note: while running roslaunch, both publisher and subscriber nodes are
running simultaneously

we can feel this on running rosnode list and rostopic list

About RQT Tool:

command: rqt

we can examine relationship between publisher node, subscriber node and
topics.

PLAY with [Turle sim](https://wiki.ros.org/turtlesim), it is really
crazy!!\
Turtle sim automatically publisher/subscribe topic (check -- rostopic
info), just we only need to create publisher/subscriber node to publish
topics accordingly.

\- just to move turtle in x direction

\- just check rostopic echo

![](images/Pictures/100002010000028A00000146B59C2EDFFABDEC1F.png){width="11.321cm"
height="5.676cm"}

![](images/Pictures/10000201000002AE0000020ECD7230F8C143FD33.png){width="11.405cm"
height="8.745cm"}

![](images/Pictures/100002010000054800000294CD2C2D48C15302F5.png){width="17cm"
height="8.297cm"}

Client and Server

\- client request for service from the server \| server is mandatory

\- request and response

creating server-client package:\

![](images/Pictures/1000020100000236000002110D7A447D48A3AAE5.png){width="10.418cm"
height="9.737cm"}

![](images/Pictures/1000020100000219000001B611151922A4610FAC.png){width="12.109cm"
height="9.876cm"}

![](images/Pictures/100002010000027B00000268A801AF1CDE3F1745.png){width="12.247cm"
height="11.88cm"}

rosservice call \<service\_name\> "date: true/false"

Note: in publish and subscribe -- there is no need for subscriber all
time

search in ros installation for service

computer/opt/ros/noetic/share/std\_srvs

we can say \~ msgs are subset of services

\
ROS Parameter Server:

\- associated with roscore

\- stores parameter

![](images/Pictures/100002010000029E0000027788EEA72C11FF78AB.png){width="13.57cm"
height="12.778cm"}

Notes:

we cannot do this everytime in terminal. We need this in some automated
scripts

we can only get this running only from roslaunch command

we need to create 'yaml' file -- basically a database

Create -- Ros Param Yaml File

![](images/Pictures/100002010000013000000075B34CCE77EDBD2903.png){width="6.553cm"
height="2.522cm"}

Simillary like, to run many topic at a particular time -- we use ros
launch file.

We need to include this yaml file aslo there in launch file

create -- Launch File (for param (yaml file))

![](images/Pictures/100002010000035A0000008B2E24AACB150F6AA0.png){width="15.633cm"
height="2.533cm"}

running launch file:

![](images/Pictures/10000201000002990000029370225C5899F8BE7D.png){width="13.376cm"
height="13.256cm"}

Here, in launch file, path of config is little tedious (not same for
everyone)

edit like this

![](images/Pictures/10000201000002C00000007E13C5F1F7E0007270.png){width="13.693cm"
height="2.45cm"}

Rosbags:\

Bags for storing ros-data

\- run roscore

\- record rosbag

\- publish topic varibales

\- play rosbag (where you can see traces)

\- rostopic echo and look for traces

![](images/Pictures/10000201000002980000028191E7F81811320D8F.png){width="13.305cm"
height="12.845cm"}

create python file to view bags contents instead of echoing

read\_bag file:

![](images/Pictures/100002010000031C0000012E9AB68057BDA50987.png){width="13.34cm"
height="5.061cm"}

output:

![](images/Pictures/10000201000002320000011C0A7FDBA03D2912FB.png){width="10.716cm"
height="5.415cm"}

Quick Collective Works:\

publisher:

![](images/Pictures/100002010000029E0000017BC40001BDD92D7EE4.png){width="11.718cm"
height="6.627cm"}

subscriber:

![](images/Pictures/100002010000031E00000167B47D7202D70E3C8E.png){width="14.258cm"
height="6.414cm"}

launch:

![](images/Pictures/100002010000038400000099EA502A3F90B27D49.png){width="17cm"
height="2.889cm"}

read bag:\
\
![](images/Pictures/100002010000031B0000023802A0E17C3AA8654D.png){width="14.575cm"
height="10.414cm"}

running roscore:

recording rosbags with all topics:\
\
![](images/Pictures/1000020100000268000001197BD511256DF508B2.png){width="14.28cm"
height="6.514cm"}

running launch file:

![](images/Pictures/10000201000002730000008180B102D84F7734E4.png){width="15.145cm"
height="3.117cm"}

Playing rosbag:\

![](images/Pictures/10000201000001E5000002582AA2084BE90965D8.png){width="12.832cm"
height="15.875cm"}\
