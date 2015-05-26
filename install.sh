cp ./copy.sh /usr/sbin/rpi-photo-copy.sh
chmod u+x /usr/sbin/rpi-photo-copy.sh
cp ./monitor.py /usr/sbin/rpi-photo-monitor.py
chmod u+x /usr/sbin/rpi-photo-monitor.py
cp ./init.d/copy /etc/init.d/rpi-photo-copy
cp ./init.d/monitor /etc/init.d/rpi-photo-monitor

#try to enable through chkconfig
chkconfig -a rpi-photo-copy
chkconfig -a rpi-photo-monitor
