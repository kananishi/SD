import socket, select
from constCS import *
port = 32000
host = HOST

#Function to send message to all connected clients
def send_to_all (sock, message):
    #Message not forwarded to server and sender itself
    for socket in connected_list:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # if connection not available
                socket.close()
                connected_list.remove(socket)

def create_connection():
    sockfd, addr = server_socket.accept()
    name=sockfd.recv(buffer)
    connected_list.append(sockfd)
    record[addr]=""
   
    #add name and address
    record[addr]=name

    sockfd.send(b"Welcome to chat room. Enter 'tata' anytime to exit\n")
    send_to_all(sockfd, name+b" joined the conversation \n")

def msg_arrived(sock):
    # Data from client
    data1 = sock.recv(buffer)
    #print "sock is: ",sock
    data=data1[:data1.index("\n")]
    #print "\ndata received: ",data
    
    #get addr of client sending the message
    i,p=sock.getpeername()
    if data == "quit":
        msg=record[(i,p)]+" left the conversation \n"
        send_to_all(sock,msg)
        print("Client (%s, %s) is offline" % (i,p)," [",record[(i,p)],"]")
        del record[(i,p)]
        connected_list.remove(sock)
        sock.close()

    else:
        msg="\r"+record[(i,p)]+": "+"\33[0m"+data+"\n"
        send_to_all(sock,msg)
    

name=""
    
#dictionary to store address corresponding to username
record={}
#List to keep track of socket descriptors
connected_list = []
buffer = 4096

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen(10) #listen atmost 10 connection at one time

# Add server socket to the list of readable connections
connected_list.append(server_socket)
print("Servidor inicializado\n")

while True:
    # Get the list sockets which are ready to be read through select
    readable,writable,exceptional = select.select(connected_list,[],[])

    for sock in readable:
        #New connection
        if sock == server_socket:
            create_connection()

        #Some incoming message from a client
        else:
            msg_arrived(sock)

server_socket.close()


