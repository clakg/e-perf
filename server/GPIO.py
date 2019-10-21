import RPi.GPIO as GPIO
 
    # Initialisation des GPIOs
def GPIO_initialize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def GPIO_clean():
    GPIO.cleanup()