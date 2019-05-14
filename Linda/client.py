'''
    host default(loopback): $python3 client.py
    set host: $ python3 client.py <host address>
'''
import socket, select, string, sys
#import constCS
HOST = '127.0.0.1'

'''
    Helper function (formatting)
'''
def display() :
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():

    # Define the server ip adress and port
    if len(sys.argv)>2:
        host = sys.argv[1]
        
    else:
        host = HOST

    port = 32000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # Connecting host
    s.connect((host, port))

    # Asks for user name
    name=input("Enter username:")

    #if connected
    # s.send(name)
    # display()
    while True:
        socket_list = [sys.stdin, s]
        print("Press enter to conitnue")
        # Get the list of sockets which are readable
        rList, wList, error_list = select.select(socket_list , [], [])

        for sock in rList:
            #incoming message from server
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    sys.exit()
                else:
                    sys.stdout.write(str(data,'utf-8'))
                    display()

            #user entered a message
            else:
                active = input()
                service = input("Which service to use? (in, out, rd): ")
                subject = input("Enter a subject: ")
                text = ""
                if service == "in" or service == "out":
                    text = input("Enter the text: ")

                msg = "<service>"+service+"</service><user>"+name+"</user><subject>"+subject+"</subject><text>"+text+"</text>"

                s.send(msg.encode('utf-8'))

if __name__ == "__main__":
    main()
