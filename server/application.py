from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from threading import Thread
import time
from GPIO import GPIO_initialize

app = Flask(__name__)
socketio = SocketIO(app)


from movement import Movement
i=0

@app.route('/')
def index():
    return render_template('index.html')

def movementDetected():
    global i
    #socketio.emit('alert', 'Aucun probleme d\'ecoulement', Broadcast=True)
    i=0

def movementNotDetected():
    print("Mouvement non détecté!")
    socketio.emit('alert', 'Ecoulement non detecté!', Broadcast=True)

def count():
    global i
    i=0
    while True:
        i=i+1
        time.sleep(1)
        print(i)
        if i==10:
            movementNotDetected()
            i=0

def startCounting():
    thread = Thread(target = count)
    thread.start()
    return thread

GPIO_initialize()
movementSensor = Movement(17, detectFunction=movementDetected)


startCounting()
movementSensor.startDetection()

@app.route('/stop_detector')
def stopDetector():
    movementSensor.stopDetection()

@app.route('/start_detector')
def startDetector():
    movementSensor.startDetection()