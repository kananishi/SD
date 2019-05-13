import socket, select, re, linda
port = 32000
host = "localhost"

tuple_space = []
#Function to send message to all connected clients
def send_to_user (sock, message):
    #Message not forwarded to server and sender itself
    for socket in connected_list:
        if socket == sock :
            try :
                socket.send(message)
            except :
                # if connection not available
                socket.close()
                connected_list.remove(socket)

def create_connection():
    sockfd, addr = server_socket.accept()
    # name=sockfd.recv(buffer)
    connected_list.append(sockfd)
    record[addr]=""

    #add name and address
    record[addr]=name

    # sockfd.send("Welcome to chat room. Enter 'tata' anytime to exit\n")
    # send_to_all(sockfd, name+" joined the conversation \n")

def msg_arrived(sock):

    # Data from client
    data1 = sock.recv(buffer)
    #print "sock is: ",sock
    # data=data1[:data1.index("\n")]
    #print "\ndata received: ",data
    msg = ""
    service = re.search("<service>(.*)</service>",data1)
    if service:
        if service.group(1) == "out":
            user = re.search("<user>(.*)</user>",data1)
            subject = re.search("<subject>(.*)</subject>",data1)
            text = re.search("<text>(.*)</text>",data1)
            if user and subject and text:
                linda._out(tuple_space,(user.group(1),subject.group(1),text.group(1)))
                msg = "Entry created\n"
            else:
                msg =  "Failed to create entry\n"
        elif service.group(1) == "in":
            user = re.search("<user>(.*)</user>",data1)
            subject = re.search("<subject>(.*)</subject>",data1)
            text = re.search("<text>(.*)</text>",data1)
            if user and subject and text:
                msg = linda._in(tuple_space,(user.group(1),subject.group(1),text.group(1)))
            else:
                msg =  "Failed to attempt to remove entries\n"
        elif service.group(1) == "rd":
            subject = re.search("<subject>(.*)</subject>",data1)
            if subject:
                subject_entries = linda._rd(tuple_space, subject.group(1))
                if subject_entries != []:
                    msg = ""

                    for owner, text in subject_entries:
                        msg += owner + ": " + text + "\n"
                else:
                    msg = "No entries found for given subject\n"
                # print all_texts
            else:
                msg = "Failed to search entries\n"
        else:
            msg = "Invalid service\n"
    else:
        msg = "Service not found\n"

    print msg
    send_to_user(sock, msg)

    #get addr of client sending the message
    # i,p=sock.getpeername()
    # if data == "quit":
    #     msg=record[(i,p)]+" left the conversation \n"
    #     send_to_all(sock,msg)
    #     print "Client (%s, %s) is offline" % (i,p)," [",record[(i,p)],"]"
    #     del record[(i,p)]
    #     connected_list.remove(sock)
    #     sock.close()
    #
    # else:
    #     msg="\r"+record[(i,p)]+": "+"\33[0m"+data+"\n"
    #     send_to_all(sock,msg)


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
