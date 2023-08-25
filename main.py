import RPi.GPIO as GPIO

def initialize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # button
    GPIO.setup(14, GPIO.OUT)  # red led
    GPIO.setup(15, GPIO.OUT)  # green led

def check_button():
    initialize()
    if (GPIO.input(12) == 1):
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
    else:
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        while True:
            check_button()
    except:
        initialize()
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.cleanup()