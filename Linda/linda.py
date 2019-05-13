import socket
import select, string, sys
from constCS import * #-


clients = []
msg_to_send = []

#Helper function (formatting)
def display() :
    you="You: " 
    sys.stdout.write(you)
    sys.stdout.flush()

def connect():
	if len(sys.argv)<2:
		host = HOST
	else:
		host = sys.argv[1]

	port = 32000

	#asks for user name
	name=input("CREATING NEW ID:\n Enter username: ")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	# connecting host
	s.connect((host, port))

	#if connected
	s.send(name.encode('utf-8'))
	display()

	return s,name



def out(usr, tpc, msg):
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((HOST, PORT)) # connect to server (block until accepted)
	s.send(usr)
	usrAsw = s.recv(1024)

	s.send(tpc)
	tpcAsw = s.recv(1024)
	
	if str(tpc) == str(tpcAsw):
		s.send(msg)
		msgAsw = s.recv(1024)

		print(usrAsw)
		print(tpcAsw)
		print(msgAsw)

	s.close()

def linda_universe_rcv():
	s = socket(AF_INET, SOCK_STREAM)
	s.bind((HOST, PORT))  #-
	s.listen(1)      

	while True:     #-
		(conn, addr) = s.accept()  # returns new socket and addr. client
		
		if conn not in clients:
			clients.append(conn)

		for c in clients:
			usr = c.recv(1024)   # receive data from client
			print(usr)
			if not usr: break       # stop if client stopped
			c.send(str(usr)) # return sent data plus an "*"

			tpc = c.recv(1024)   # receive data from client
			if not tpc: break       # stop if client stopped
			c.send(str(tpc)) # return sent data plus an "*
				
			msg = c.recv(1024)   # receive data from client
			if not usr: break       # stop if client stopped
			c.send(str(msg)) # return sent data plus an "*

			msg_to_send.append((usr, tpc, msg))

		for oc in clients:
			for msg in msg_to_send:
				oc.send(msg_to_send[0])
				oc.send(msg_to_send[1])
				oc.send(msg_to_send[2])

	conn.close()               # close the connection
