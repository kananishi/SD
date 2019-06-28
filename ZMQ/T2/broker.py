import zmq

def main():
    context = zmq.Context(1)
        # Socket facing clients
    frontend = context.socket(zmq.SUB)
    frontend.bind("tcp://*:5559")

    frontend.setsockopt_string(zmq.SUBSCRIBE, "")

    # Socket facing services
    backend = context.socket(zmq.PUB)
    backend.bind("tcp://*:5560")

    zmq.proxy(frontend, backend)


if __name__ == "__main__":
    main()
