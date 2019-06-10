import sys
import zmq
import time
from multiprocessing import Process
import random
import markets_companies

def pub(process_id):
	port = "5559"
	context = zmq.Context()
	socket = context.socket(zmq.PUB)
	socket.connect("tcp://localhost:%s" % port)
	while True:
		#publisher_id = random.randrange(0,9999)
		#topic = random.randrange(1,10)
		messagedata = markets_companies.markets[process_id]
		for i in range(0, len(markets_companies.companies[markets_companies.markets[process_id]])):
			messagedata += " "+markets_companies.companies[markets_companies.markets[process_id]][i]
		print("%s %s" % (process_id, messagedata))
		socket.send_string("%d %s" % (process_id, messagedata))
		time.sleep(1)

def main():
	for i in range(0,8):
		process = Process(target=pub, args = (i,))
		process.start()
		#process.join()

if __name__ == '__main__':
	main()
