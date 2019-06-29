import zmq

def main():
    context = zmq.Context(1)
    # Socket facing clients
    # Recebe do publishers
    frontend = context.socket(zmq.SUB)
    frontend.bind("tcp://*:5559")
    # Recebe todos os topicos
    frontend.setsockopt_string(zmq.SUBSCRIBE, "")

    # Socket facing services
    # Envia mensagens para subscribers
    backend = context.socket(zmq.PUB)
    backend.bind("tcp://*:5560")

    # Start proxy - repassa mensagens do frontend para o backend
    zmq.proxy(frontend, backend)

if __name__ == "__main__":
    main()
