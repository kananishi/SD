'''
    $ python3 server.py
'''
import socket, select, re, linda

port = 32000
host = "127.0.0.1"

tuple_space = []

'''
    Send message to specific user
'''
def send_to_user (sock, message):
    #Message not forwarded to server and sender itself
    for socket in connected_list:
        if socket == sock :
            try :
                socket.send(message.encode('utf-8'))
            except :
                # if connection not available
                socket.close()
                connected_list.remove(socket)

'''
    Create a conection between a client and the server
    if the connection is accepted append the client to the list of connected
'''
def create_connection():
    sockfd, addr = server_socket.accept()
    # name=sockfd.recv(buffer)
    connected_list.append(sockfd)
    record[addr]=""

    #add name and address
    record[addr]=name

    # sockfd.send("Welcome to chat room. Enter 'tata' anytime to exit\n")
    # send_to_all(sockfd, name+" joined the conversation \n")

'''
    Receive and process a message arrived
'''
def msg_arrived(sock):

    # Data from client
    # Data format: <service:out,in,rd> <user_name> <subject> <text>
    data = sock.recv(buffer)
    data1 = str(data,'utf-8')
    # System message
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

    print(msg)
    send_to_user(sock, msg)


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

if __name__ == "__main__":
    main()