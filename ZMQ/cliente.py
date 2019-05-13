import zmq 
context = zmq.Context()

HOST = "127.0.0.1"
PORT = "8888"
php = "tcp://" + HOST + ":" + PORT
s = context.socket(zmq.REQ)

s.connect(php)
s.send_string("Hello World")
message = s.recv()
s.send_string("STOP")

print (message)
