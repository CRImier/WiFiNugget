# WiFiNugget

Binaries &amp; source code for the Wi-Fi Nugget

![Hell yeah](https://cdn.shopify.com/s/files/1/2779/8142/products/signal-2021-09-30-162945_1024x1024.jpg?v=1633047834)

Documentation: https://github.com/skickar/WiFiNugget/wiki


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




