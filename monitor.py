import RPi.GPIO as GPIO
import time
import picamera
import subprocess
from pyslack import SlackClient

addr = subprocess.check_output("ifconfig wlan0 | grep inet", shell=True)

tag=subprocess.check_output(("date", "+%m%d%y%H%M%S")).rstrip()
started = False
running = False
run=0
frame=0

client = None 
while client == None:
	try:
		client = SlackClient('xoxp-2222178975-2227657186-2585667366-7b182a')
	except:
		print "Error connecting to slack:", sys.exc_info()[0]
	time.sleep(1)

client.chat_post_message('@rlankenau', "TimeLapse just booted: {0}".format(addr), username='slackbot')

FRAMES_PER_HOUR = 600

cam = picamera.PiCamera()
cam.led = False
cam.vflip = True
time.sleep(2)


def capture_frame(r, f):
	global tag
	global cam
	cam.capture('/var/www/{2}-frame{0:03d}{1:08d}.jpg'.format(r,f,tag))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def buttonPress(channel):
	global running
	global run
	global frame
	if running:
		running = False
	else:
		run += 1
		frame = 0;
		running = True

GPIO.add_event_detect(11, GPIO.RISING, callback=buttonPress, bouncetime=2000)

while True:
	start = time.time()
	if running:
		if started == False:
			client.chat_post_message('@rlankenau', "TimeLapse just started run {0}".format(run), username='slackbot')
		started = True
		capture_frame(run,frame)
		GPIO.output(12, True)
		time.sleep(.5)
		GPIO.output(12, False)
		frame += 1
	elif started == True:
		client.chat_post_message('@rlankenau', "TimeLapse just ended run {0} with {1} frames".format(run,(frame+1)), username='slackbot')
		started = False

	time.sleep(int(60*60/FRAMES_PER_HOUR) - (time.time() - start))

GPIO.cleanup()

