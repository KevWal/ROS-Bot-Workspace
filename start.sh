#!/bin/sh

if uhubctl | grep -q "Port 2: 0080 off" ;
then
	echo "Turning USB port power on"
	sudo uhubctl --action on -l 2 > /dev/null
	sleep 6
else
	echo "USB Power already on"
fi

roslaunch edukit_bot bringup.launch
