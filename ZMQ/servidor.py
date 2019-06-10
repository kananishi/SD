import zmq
context = zmq.Context()

HOST = "127.0.0.1"
PORT1 = "8886"
PORT2 = "8887"
p1 = "tcp://"+ HOST + ":" + PORT1
p2 = "tcp://"+ HOST + ":" + PORT2
s = context.socket(zmq.REP)

s.connect(p1)
s.bind(p2)

while True:
	message = s.recv()
	print(message)
	if not b"STOP" == message:
		s.send_string(str(message,'utf-8'))
	else:
		break
