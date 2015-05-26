#!/bin/bash

cd /var/photos/

while true
do

	for file in `ls -1 /var/photos/`
	do
		scp $file rlankenau@wintermute:photos/$file
		if [ $? -eq 0 ]; then
			rm -f $file
		fi
	done
	sleep 600
done
