#!/bin/sh
esptool.py --port /dev/ttyUSB0 --baud 460800 read_flash 0 0x400000 wifinugget_upy_v3.bin
