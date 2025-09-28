# rené

A [Magritte](https://github.com/decarbonization/magritte) front end that runs on embedded Linux devices like the Raspberry Pi.

## BOM

- [Raspberry Pi Zero 2 W with Header](https://www.adafruit.com/product/6008)
- [Adafruit PiTFT Plus 320x240 2.8" TFT + Capacitive Touchscreen](https://www.adafruit.com/product/2423)
- An SD card with a capacity of at least 128 GB

### For Battery Power

- [PowerBoost 1000 Charger - Rechargeable 5V Lipo USB Boost @ 1A - 1000C](https://www.adafruit.com/product/2465)
- [Lithium Ion Cylindrical Battery - 3.7v 2200mAh](https://www.adafruit.com/product/1781)

### Optional

- [Breadboard-friendly SPDT Slide Switch](https://www.adafruit.com/product/805): To be able to turn off raspi without unplugging it from the PowerBoost 1000
- [Terminal Block - 2-pin 3.5mm - pack of 5!](https://www.adafruit.com/product/724): To be able to easily tap into +5V and GND from the PowerBoost 1000
- [Silicone Cover Stranded-Core Wire - 26AWG in Various Colors](https://www.adafruit.com/product/1970): To be able to solder the low battery sense pin to the raspi
- [USB OTG Host Cable - MicroB OTG male to A female](https://www.adafruit.com/product/1099): To be able to connect a keyboard and/or DAC to the raspi

## Prerequisites

- Install the PiTFT Plus touchscreen onto the Raspberry Pi Zero 2 W
- Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to prepare the SD card
    1. Choose "Raspberry Pi Zero 2 W" for "Raspberry Pi Device"
    2. Choose "Raspberry Pi OS Lite (64-bit)" under "Raspberry Pi OS (other)" for "Operating System"
    3. Choose your SD card under storage. **Warning:** The contents of the SD card will be erased
    4. Press "Next"
    5. When prompted to apply OS customization settings, choose "Edit Settings"
    6. Set the hostname to a known value such as 'rene-pi'
    7. Set the username and password to known values such as 'mobile' and 'alpine'
    8. Configure your wireless LAN credentials and locale settings
    9. Under the services tab, enable SSH with password authentication
    10. Save the settings then choose "Yes" on the "Edit Settings" prompt
    11. Write the SD card
- Install the SD card into the Raspberry Pi. **Caution:** It's very easy to snap the end of the SD card and destroy it once inserted into the pi
- Plug in the Raspberry Pi and wait for it to boot up
- SSH into the Raspberry Pi from your computer like e.g. `ssh mobile@rene-pi.local` and enter your password when prompted
- Copy the `pi/` directory to the Raspberry Pi and run `./pi/setup.sh`

The Raspberry Pi may reboot multiple times. SSH back in and run `./pi/setup.sh` until the device reboots into a graphical environment on the touch screen.

