import zmq

HOST = "127.0.0.1"
PORT = "8888"

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")

for i in range(5):
	time = s.recv()
	print(time)
