#!/bin/bash

# Enable halt on error
set -e

# Make sure we're in `pi/`
cd "$(dirname "$0")"

# Upgrade the system
echo "- Upgrading system, device may reboot"
sudo apt update && sudo apt upgrade
[ -e /var/run/reboot-required ] && sudo reboot

# Install graphical environment
sudo apt install -y seatd sway foot
sudo systemctl enable seatd.service
sudo systemctl start seatd.service
sudo groupadd seat
sudo usermod -a -G seat "$(whoami)"

# TODO: Write bash profile
# TODO: Copy bash profile and sway configurations

# Set up venv for Adafruit
echo "- Setting up python venv"
sudo apt install python3-venv
python -m venv env --system-site-packages
source env/bin/activate

# Install Adafruit dependencies
echo "- Install required Adafruit dependencies"
sudo apt-get install -y git python3-pip
pip3 install --upgrade adafruit-python-shell click

# Download Adafruit installer script
echo "- Downloading Adafruit installer"
git clone https://github.com/adafruit/Raspberry-Pi-Installer-Scripts.git

# Run Adafruit installer script
echo "- Running Adafruit installer, device will reboot"
cd Raspberry-Pi-Installer-Scripts
sudo -E env PATH=$PATH python3 adafruit-pitft.py --display=28c --rotation=0 --install-type=mirror --reboot=yes

# Install pigpio to be able to control screen backlight
sudo apt-get install pigpio python3-pigpio
sudo systemctl enable pigpiod
sudo systemctl start pigpiod

