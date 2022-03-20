from whyteweb import Serve

server = Serve("127.0.0.1", 5000)


@server.Route('/', None)
def index():
    return "Hello, World"


server.start()
