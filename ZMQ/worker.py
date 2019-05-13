import zmq, time, pickle, sys

SRC1 = "127.0.0.1"
SRC2 = "127.0.0.2"
PORT1 = "8888"
PORT2 = "8889"

context = zmq.Context()
me = str(sys.argv[1])
r = context.socket(zmq.PULL)
p1 = "tcp://" + SRC1 + ":" + PORT1
p2 = "tcp://" + SRC2 + ":" + PORT2
r.connect(p1)
r.connect(p2)

i = 0
while True:
	work = pickle.loads(r.recv())
	time.sleep(work[1]*0.01)
	print(i)
	i += 1
