# WiFiNugget
Binaries & source code for the Wi-Fi Nugget

MicroPython scripts:

* `NeopixelTest.py` - short script for testing an attached Neopixel strip
* `NeopixelTest_CircuitPython.py` - short script for testing an attached Neopixel strip (in CircuitPython)
* `EverythingTest.py` - test of SH1106 screen, Neopixel and buttons
* `Example.py` - example of a `hw.py`-based script that you can use to build your scripts from.
* `hw.py` - Nugget hardware definition library to make coding easier; has I2C, OLED screen, Neopixel and Wemos D0-D8 pin number definitions. Need to put button debounce there for it to be complete.
* `pack_unpack_test.py` - image compression/decompression playground&test file, for developing the compression code that makes display images consume less RAM

MicroPython libraries used:
* `sh1106.py` - [robert-hh's SH1106 library](https://github.com/robert-hh/SH1106/)
