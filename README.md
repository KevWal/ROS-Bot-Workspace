# My ROS Robot Project

Raspberry Pi based robot running ROS1 Noetic (LTS) on Ubuntu Focal 20.04 64bit (LTS) with motor drivers and encoders connected directly to the Pi.


![ROS1 Robot](https://raw.githubusercontent.com/KevWal/ROS-Bot-Workspace/master/media/robot.jpg "ROS1 Robot")

Edit main [bringup.launch](https://github.com/KevWal/ROS-Bot-Workspace/blob/master/src/edukit_bot/launch/bringup.launch) file and select one of:
  * test_odom - Just for testing different odometry sources against Lidar to see how accurate it is
  * hector_mapping - Generate a map using hector_mapping and joystick to drive
  * navigation_stack - Encoder odometry, map_server static map, AMCL localisation & move_base navigation stack
  * gmapnav - Encoder odometry, gmapping live mapping and localisation & move_base navigation stack 
  * hectornav - Hector odometry, live mapping and localisation & move_base nav with explore_lite self exploration
  * amclhectornav - Hector odometry, map_server static map, AMCL localisation & move_base navigation stack
  * cartographer - Encoder odometry, Cartographer live mapping and localisation
then run with: 'roslaunch edukit_bot bringup.launch'


Notes:
* My encoder based odometry (and associated transform) has never been very accurate, despite lots of work in that area (encoders fixed and confirmation that Pi is seeing every pulse)
* If you are having encoder issues, use an oscilloscope to check the encoders are pulsing correctly, and push the magnets closer to the sensors if you have issues with missing pulses
* Hector works well at the slow speeds my robot moves at and produces the best odometry I have had - hence I use it in later launch options
* Launch options of hectornav (for live mapping) and amclhectornav (for localisation to an existing map) work pretty well, with explore_lite giving navigation goals to move_base to do self exploration too
* cartographer looked promising, but is very complicated to configure and didn't localise at all well when turning
* I always ran graphical stuff (rviz, rqt_graph, etc) from a VM on the PC, not from Pi
* Best motors I found were 6v B45 603 ratio 30 RPM Micro Metal Gear Motors like these [these - aliexpress](https://www.aliexpress.com/item/1005001608344100.html) or [these - amazon](https://www.amazon.co.uk/dp/B0BG1K8CK1)


Example early map from Hector:
![Hector Map](https://raw.githubusercontent.com/KevWal/ROS-Bot-Workspace/master/media/map.jpg "Hector map")


Usefull files:
* Setup info and usefull commands I have listed here: [https://github.com/KevWal/ROS-Bot-Workspace/blob/master/etc/update-motd.d/motd.txt](https://github.com/KevWal/ROS-Bot-Workspace/blob/master/etc/update-motd.d/motd.txt)
* Fan setup: [https://github.com/KevWal/ROS-Bot-Workspace/blob/master/boot/firmware/usercfg.txt](https://github.com/KevWal/ROS-Bot-Workspace/blob/master/boot/firmware/usercfg.txt)
* USB Power off on boot (to save Lidar spinning endlessly) [https://github.com/KevWal/ROS-Bot-Workspace/blob/master/etc/rc.local](https://github.com/KevWal/ROS-Bot-Workspace/blob/master/etc/rc.local)
* An example layout of frames [https://github.com/KevWal/ROS-Bot-Workspace/blob/master/Frames.txt](https://github.com/KevWal/ROS-Bot-Workspace/blob/master/Frames.txt)
* All of my ROS nodes, parameters and launch files [https://github.com/KevWal/ROS-Bot-Workspace/tree/master/src/edukit_bot](https://github.com/KevWal/ROS-Bot-Workspace/tree/master/src/edukit_bot)

