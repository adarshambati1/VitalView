#!/bin/bash

echo "What is your weight? "
read weight

echo "What is your height? "
read height

echo "What is your age? "
read age

/usr/bin/python /home/pi/pulse/webcam-pulse-detector/get_pulse.py --height $height --weight $weight --age $age& 

/usr/bin/python /home/pi/rgbmatrix5x5-python/examples/rainbow.py &

/usr/bin/python /home/pi/newvital/respiratory/respiratory.py &
/usr/bin/python /home/pi/newvital/respiratory/oximeter.py &

/home/pi/pimoroni/mlx90640-library/examples/test-values-grab


