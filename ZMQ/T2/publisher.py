import sys
import zmq
import time
from multiprocessing import Process
import random
import markets_companies

""" 
Funcao pub
	atualiza o valor das acoes de um mercado
	Recebe como parametros o mercado e o intervalo de tempo em que o valor das acoes sera atualizado	
"""
def pub(process_id, sleep_time):
	# Cria conexao com o broker(proxy)
	port = "5559"
	context = zmq.Context()
	socket = context.socket(zmq.PUB)
	socket.connect("tcp://localhost:%s" % port)
	
	stock_value = []
	while True:
		#publisher_id = random.randrange(0,9999)
		#topic = random.randrange(1,10)
		#messagedata = markets_companies.markets[process_id]
		messagedata = ""
		logMessage = ""
		# Atualiza o valor de cada acao com um valor aleatorio
		for i in range(0, len(markets_companies.companies[markets_companies.markets[process_id]])):
			if len(stock_value) < len(markets_companies.companies[markets_companies.markets[process_id]]):
				stock_value.append(random.randrange(100, 999999)/100)
			else:
				stock_value[i] = stock_value[i] + random.choice([1,-1])*stock_value[i]*random.randrange(0, 30)/100
			messagedata += "<stock"+str(i)+">"+str(stock_value[i])+"</stock"+str(i)+">"
			logMessage += markets_companies.companies[markets_companies.markets[process_id]][i] +": "+ str(stock_value[i])+"\n"

		print("%s\n%s" % (markets_companies.markets[process_id], logMessage))
		# envia o valor da acoes ao broker
		socket.send_string("%d %s" % (process_id, messagedata))
		# Aguarda o intervalo de tempo definido 
		time.sleep(sleep_time)

def main():
	# Atualiza o valor das acoes da lista de mercados
	# Cria uma thread para cada mercado de acoes
	for i in range(0,len(markets_companies.markets)):
		process = Process(target=pub, args = (i, int(sys.argv[1])))
		process.start()
		#process.join()

if __name__ == '__main__':
	main()
