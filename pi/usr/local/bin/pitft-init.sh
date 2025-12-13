#!/bin/bash

# Wait a moment for pigpiod to be fully ready
sleep 1

# Set PWM frequency
pigs pfs 18 2000

# Set initial brightness (50%)
pigs p 18 128

# Show boot splash screen until wayland starts
fbi -T 2 -d /dev/fb1 -noverbose -a /usr/local/share/pitft/boot-splash.jpg
fbi -T 2 -d /dev/fb2 -noverbose -a /usr/local/share/pitft/boot-splash.jpg
