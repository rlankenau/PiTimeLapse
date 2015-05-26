#!/bin/bash

cd /var/photos/

logger -t rpi-photo-copy Started service.
while true
do

	for file in `ls -1 /var/photos/`
	do
		export OUTPUT=`scp -i /home/pi/.ssh/id_rsa $file rlankenau@wintermute:photos/$file`
		if [ $? -eq 0 ]; then
			logger -t rpi-photo-copy Copied $file to remote server, deleting.
			rm -f $file
		else
			logger -t rpi-photo-copy Failed to copy $file: $OUTPUT
		fi
	done
	sleep 600
done
