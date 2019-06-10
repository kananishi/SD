import sys
import zmq
import time
from multiprocessing import Process
import random



def sub(process_id):
	port = "5560"
	# Socket to talk to server
	context = zmq.Context()
	socket = context.socket(zmq.SUB)
	print("Collecting updates from server...")
	socket.connect ("tcp://localhost:%s" % port)
	topicfilter = process_id
	socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
	while True:
	    string = socket.recv()
	    topic, messagedata = string.split()
	    print(topic, messagedata)


def main():
	process = Process(target=sub, args = (sys.argv[1]))
	process.start()
	process.join()


if __name__ == '__main__':
	main()
