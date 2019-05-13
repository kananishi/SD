import socket, select, string, sys
import linda

def main():

    blog,name = linda.connect()
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
                    sys.stdout.write(str(data,'utf-8'))
                    linda.display()
        
            #user entered a message
            else :
		msg=sys.stdin.readline()
                #s.send(msg.encode('utf-8'))
                #linda.display()
		topic = sys.stdin.readline()

                linda.out(blog,name,topic,msg)
if __name__ == "__main__":
    main()
