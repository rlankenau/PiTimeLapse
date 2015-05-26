import RPi.GPIO as GPIO
import time
import picamera
import subprocess

started = False
running = False
run=0
frame=0

FRAMES_PER_HOUR = 600

cam = picamera.PiCamera()
cam.led = False
cam.vflip = True
time.sleep(2)

tag = time.time()


def capture_frame(r, f):
	global tag
	global cam
	cam.capture('/var/photos/{2}-frame{0:03d}{1:08d}.jpg'.format(r,f,tag))

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def buttonPress(channel):
	print "Button pressed."
	global running
	global run
	global frame
	if running:
		running = False
	else:
		run += 1
		frame = 0;
		running = True

GPIO.add_event_detect(17, GPIO.RISING, callback=buttonPress, bouncetime=2000)
print "Ready for input"

while True:
	start = time.time()
	if running:
		started = True
		capture_frame(run,frame)
		GPIO.output(18, True)
		time.sleep(.5)
		GPIO.output(18, False)
		frame += 1
	elif started == True:
		started = False

	time.sleep(int(60*60/FRAMES_PER_HOUR) - (time.time() - start))

GPIO.cleanup()

