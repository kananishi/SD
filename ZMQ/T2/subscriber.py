import sys
import zmq
import time
from multiprocessing import Process
import random
import markets_companies
from os import system
import re
from datetime import datetime
from decimal import Decimal

def sub(process_id):
	port = "5560"
	# Socket to talk to server
	context = zmq.Context()
	socket = context.socket(zmq.SUB)

	# Conecta-se ao broker(proxy)
	print("Collecting updates from server...")
	socket.connect ("tcp://localhost:%s" % port)

	# filtra as mensagens de acordo com o mercado escolhido
	topicfilter = process_id
	socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
	while True:
		string = socket.recv()
		topic, messagedata =string.split()
		_ = system("clear")
		print(markets_companies.markets[int(process_id)]+"("+str(datetime.date(datetime.now()))+" "+str(datetime.time(datetime.now()))+")"+"\n")
		for i in range(0, len(markets_companies.companies[markets_companies.markets[int(process_id)]])):
			stock = re.search(str.encode("<stock"+str(i)+">(.*)</stock"+str(i)+">"),messagedata)
			stock_value = Decimal(float(stock.group(1)))
			print(markets_companies.companies[markets_companies.markets[int(process_id)]][i]+": $"+str(round(stock_value, 2)))


def main():

	# Seleciona as acoes de qual mercado deseja-se visualizar
	print("Escolha um mercado da lista usando seu numero:")
	for m in range(0, len(markets_companies.markets)):
		print(str(m)+". "+markets_companies.markets[m])

	topic = input()
	_ = system("clear")
	sub(topic)


if __name__ == '__main__':
	main()