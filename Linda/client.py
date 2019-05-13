import socket, select, string, sys

#Helper function (formatting)
def display() :
    you="You: "
    sys.stdout.write(you)
    sys.stdout.flush()

def main():

    if len(sys.argv)<2:
        host = raw_input("Enter host ip address: ")
    else:
        host = sys.argv[1]

    port = 32000

    #asks for user name
    name=raw_input("Enter username: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connecting host
    s.connect((host, port))

    #if connected
    # s.send(name)
    # display()
    while 1:
        socket_list = [sys.stdin, s]

        # Get the list of sockets which are readable
        rList, wList, error_list = select.select(socket_list , [], [])

        for sock in rList:
            #incoming message from server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    # display()

            #user entered a message
            else :
                service = raw_input("Which service to use? (in, out, rd) ")
                subject = raw_input("Enter a subject: ")
                text = ""
                if service == "in" or service == "out":
                    text = raw_input("Enter the text: ")

                msg = "<service>"+service+"</service><user>"+name+"</user><subject>"+subject+"</subject><text>"+text+"</text>"

                s.send(msg)
                # display()

if __name__ == "__main__":
    main()
