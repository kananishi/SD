import zmq, time, pickle, sys, random

SRC1 = "127.0.0.1"
SRC2 = "127.0.0.2"
PORT1 = "8888"
PORT2 = "8889"

context = zmq.Context()
me = str(sys.argv[1])
s = context.socket(zmq.PUSH)
src = SRC1 if me == '1' else SRC2
prt = PORT1 if me =='1' else PORT2
p = "tcp://" + src + ":" + prt
s.bind(p)

for i in range(100):
	workload = random.randint(1,100)
	s.send(pickle.dumps((me,workload)))
	print(workload)
