import threading

def mytimer(): 
   print("Rien ne coule\n")

my_timer = threading.Timer(10.0, mytimer) 
my_timer.start() 
print("tout se passe bien\n") 


movementSensor = Movement(17, detectFunction=movementDetected)
count = Movement(17).startCounting()
movementSensor.startDetection()