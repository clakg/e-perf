from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from threading import Thread
import time
from GPIO import GPIO_initialize

app = Flask(__name__)
socketio = SocketIO(app)

from movement import Movement


@app.route('/')
def index():
    return render_template('index.html')

def movementDetected():
    socketio.emit('alert', 'Aucun probleme d\'ecoulement', Broadcast=True)

def movementNotDetected():
    print("Mouvement non détecté!")
    #socketio.emit('alert', 'Ecoulement non detecté!', Broadcast=True)

def count(self):
    i=0
    print('count se lance')
    while True:
        i=i+1
        time.sleep(6)
        print(i)
        if movementDetected():
            i=0
        elif i==10:
            return movementNotDetected()

def startCounting(self):
    thread = Thread(target = self.count)
    thread.start()
    return thread

GPIO_initialize()
movementSensor = Movement(17, detectFunction=movementDetected)
c = startCounting()

c.join()
movementSensor.join()
movementSensor.startDetection()

@app.route('/stop_detector')
def stopDetector():
    movementSensor.stopDetection()

@app.route('/start_detector')
def startDetector():
    movementSensor.startDetection()

    