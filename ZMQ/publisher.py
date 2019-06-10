import zmq, time

HOST = "127.0.0.1"
PORT = "8886"

context = zmq.Context()
s = context.socket(zmq.PUB)
p = "tcp://"+ HOST + ":" + PORT
s.bind(p)

while True:
	time.sleep(5)
	s.send_string("TIME"+ time.asctime())
	print(time.asctime())
