from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from threading import Thread
from GPIO import GPIO_initialize

app = Flask(__name__)
socketio = SocketIO(app)

from movement import Movement


@app.route('/')
def index():
    return render_template('index.html')

def movementDetected():
    socketio.emit('alert', 'Aucun probleme d\'ecoulement', Broadcast=True)

GPIO_initialize()
movementSensor = Movement(17, detectFunction=movementDetected)
movementSensor.startDetection()


@app.route('/stop_detector')
def stopDetector():
    movementSensor.stopDetection()

@app.route('/start_detector')
def startDetector():
    movementSensor.startDetection()