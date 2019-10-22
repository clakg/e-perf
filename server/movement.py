import RPi.GPIO as GPIO
from led import Led
from GPIO import GPIO_initialize
import time
from threading import Thread

class Movement:

    def __init__(self, numGPIO, detectFunction = None, readyFunction = None):
        self.numGPIO = numGPIO
        GPIO.setup(self.numGPIO, GPIO.IN)
        self.running = False
        self.detectFunction = detectFunction
        self.readyFunction = readyFunction
        countingStart = False

    def detect(self):
        currentstate = 0
        previousstate = 0
        redLed = Led(18)
        blueLed = Led(24)
        
        while self.running:
            # Lecture du capteur
            currentstate = GPIO.input(self.numGPIO)
            countingStart = True
            # Si le capteur est déclenché
            if currentstate == 1 and previousstate == 0:
                print("    Ca coule bien !")
                redLed.off()
                blueLed.asyncOn()
                if not (self.detectFunction is None):
                    self.detectFunction()
                # En enregistrer l'état
                previousstate = 1
            # Si le capteur s'est stabilisé
            elif currentstate == 0 and previousstate == 1:
                print("    Ca ne coule plus !")
                blueLed.off()
                redLed.asyncOn()
                if not (self.readyFunction is None):
                    self.readyFunction()
                previousstate = 0
            # On attends 10ms
            #time.sleep(0.01)

    def startDetection(self):
        self.running = True
        thread = Thread(target=self.detect)
        thread.start()
        return thread
    
    def stopDetection(self):
        self.running = False