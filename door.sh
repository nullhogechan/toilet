#!/bin/sh

date > /var/log/toilet/date

paste /var/log/toilet/date /var/log/toilet/toilet1 /sys/class/gpio/gpio18/value >> /var/log/toilet/door.log

paste /sys/class/gpio/gpio18/value > /var/log/toilet/door_use.log

