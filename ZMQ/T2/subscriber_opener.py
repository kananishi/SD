import sys
import zmq
import time
from multiprocessing import Process
import random
import markets_companies
from subprocess import Popen, PIPE
import os
import re

def main():

	subscriber_script = "subscriber.py"

	for i in range(0, int(sys.argv[1])):
		cwd = os.getcwd()
		# set environment, start new shell
		p = Popen(["gnome-terminal", "-e", "python3 "+cwd+"/"+subscriber_script], stdin=PIPE)   
		#p.communicate(str.encode('python3 /home/rodolfo/Desktop/ZMQ/sub.py')) # pass commands to the opened shell
	#process.join()


if __name__ == '__main__':
	main()
