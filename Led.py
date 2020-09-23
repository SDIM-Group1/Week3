import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, True)
pwm_led = GPIO.PWM(16, 500)
pwm_led.start(100)
pwm_led.ChangeDutyCycle(50)
time.sleep(2)
pwm_led.ChangeDutyCycle(100)
time.sleep(2)
GPIO.output(16, False)
GPIO.cleanup()