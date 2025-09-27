# rené

A [Magritte](https://github.com/decarbonization/magritte) front end that runs on embedded Linux devices like the Raspberry Pi.

## BOM

- [Raspberry Pi Zero 2 W with Header](https://www.adafruit.com/product/6008)
- [Adafruit PiTFT Plus 320x240 2.8" TFT + Capacitive Touchscreen](https://www.adafruit.com/product/2423)
- An SD card with a capacity of at least 128 GB

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

