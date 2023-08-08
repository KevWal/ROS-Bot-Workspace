#!/bin/sh

# Turn USB port power on
sudo uhubctl --action on -l 2

sleep 6

roslaunch edukit_bot bringup.launch
