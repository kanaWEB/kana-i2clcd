#!/bin/sh
export QUICK2WIRE_API_HOME=/home/pi/code/quick2wire/quick2wire-python-api
export PYTHONPATH=$PYTHONPATH:$QUICK2WIRE_API_HOME
DIR="$( cd "$( dirname "$0" )" && pwd )"
screenType=$1
i2cport=$2
i2cAddress=$3
echo '/usr/bin/python3 $DIR/lcd_off.py "$screenType" "$i2cport" "$i2cAddress"'
/usr/bin/python3 $DIR/lcd_off.py "$screenType" "$i2cport" "$i2cAddress"
