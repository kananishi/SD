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

	# Inicia os subscribers
	for i in range(0, int(sys.argv[1])):
		cwd = os.getcwd()
		p = Popen(["gnome-terminal", "-e", "python3 "+cwd+"/"+subscriber_script], stdin=PIPE)   # set environment, start new shell
	
if __name__ == '__main__':
	main()