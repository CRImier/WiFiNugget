# WiFiNugget

Binaries & source code for the Wi-Fi Nugget

MicroPython scripts:

* `main.py` - Example script for using the Nugget on ESP8266 hardware. Has examples for WiFi config, screen and neopixel control and button state reading. Is heavily based on `hw.py`.
* `hw.py` - Nugget hardware definition library to make coding easier; has code for the OLED screen, buttons and the Neopixel. Also has Wemos D0-D8 pin number definitions.
* `pack_unpack_test.py` - image compression/decompression playground&test file, for developing the compression code that makes display images consume less RAM. You don't need to store this on your Nugget.
* `upy_tests/NeopixelTest.py` - short script for testing an attached Neopixel strip
* `upy_tests/NeopixelTest_CircuitPython.py` - short script for testing an attached Neopixel strip (in CircuitPython)
* `upy_tests/EverythingTest.py` - test of SH1106 screen, Neopixel and buttons

MicroPython libraries used:
* `sh1106.py` - [robert-hh's SH1106 library](https://github.com/robert-hh/SH1106/)

Binaries &amp; source code for the Wi-Fi Nugget

Documentation: https://github.com/HakCat-Tech/WiFiNugget/wiki

Quickstart Setup: https://youtu.be/WAG7yCbEFtw

![Hell yeah](https://cdn.shopify.com/s/files/1/2779/8142/products/signal-2021-09-30-162945_1024x1024.jpg?v=1633047834)


**Arduino Code:**

* Wi-Fi deauthentication & dissisociation attack detector by @AlexLynd based on @spacehuhn's deauth detector (See here: https://github.com/HakCat-Tech/HaxxDetector)

* Wi-Fi Deauther - Wi-Fi scanning & attack platform for the ESP8266 by @spacehuhn (See here: https://github.com/HakCat-Tech/esp8266_deauther)

**CircuitPython Code:** (S2 Nugget Only, Does Not Work On ESP8266 Nugget!)

* CircuitNeopixelTest.py - CircuitPython Code to test and control the neopixel on the Wi-Fi nugget. 

**MicroPython Code:**

* MicroOLEDPixelTest.py  - Micropython test of SH1106 screen & built in neopixel (requires SH1106 library installed - https://github.com/robert-hh/SH1106)

**Precompiled Binaries:**

* DeauthDetector.bin - Wi-Fi deauthentication & dissociation attack detector by @AlexLynd based on @spacehuhn's deauth detector (Precompiled, flash directly with esptool)

* esp8266-20210902-v1.17.bin - Current, working MicroPython binary to flash to the Wi-Fi Nugget as of 9/30/21 (download the latest here: https://micropython.org/download/esp8266/)

* Nugget_Deauther.bin - The Wi-Fi Deauther V2.5 by @spacehuhn, modified for Nugget by @AlexLynd 

**Helper Code:**

* pack_unpack_test.py - Compress Bitmap Images for MicroPython by @CRImier