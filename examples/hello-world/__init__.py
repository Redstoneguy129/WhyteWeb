from whyteweb import Serve

with Serve("127.0.0.1", 5000) as server:
    @server.Route('/', None)
    def index():
        return "Hello, World"
    server.start()
