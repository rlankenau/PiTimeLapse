This set of scripts manages a Raspberry Pi-based time-lapse camera.  It is intended to be as dead-simple as possible.

# install.sh
Installs the scripts in the correct place to run at startup.  Must be run as root from the current directory.

# monitor.py
Daemon that drives the camera.  Also lets you turn it on and off with a button, and indicates each frame with an LED.

# copy.sh
Daemon that copies files to a remote server.  The Pi fills up pretty quickly, and doesn't really have the horsepower to crunch the images into a video, so it's better to move them to a beefier system for that.  Also cuts down on space used on the SD card.

# init.d/copy and init.d/monitor
init.d scripts for managing the copy and monitor services.

