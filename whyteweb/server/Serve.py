from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

from .Handler import RequestHandler, DOM
from .Router import Router


class Serve:
    def __init__(self, host, port):
        self.daemon = None
        self.http = None
        self.host = host
        self.port = port
        self.router = Router()

    def __enter__(self):
        self.http = HTTPServer((self.host, self.port), self.makeHandler)
        self.daemon = Thread(target=self.http.serve_forever)
        self.daemon.daemon = True
        return self

    def __exit__(self, _type, value, traceback):
        print("Server Stopped")
        if traceback is not None:
            print(value)

    def Route(self, path, dom):
        def wrap(func):
            func.path = path
            func.value = func()
            self.router.add_route(func)
            return func

        return wrap

    def get_router(self):
        return self.router

    def start(self):
        try:
            self.daemon.start()
        except AttributeError:
            self.http = HTTPServer((self.host, self.port), self.makeHandler)
            self.daemon = Thread(target=self.http.serve_forever)
            self.daemon.start()
        try:
            while True:
                if not self.daemon.is_alive():
                    return
        except KeyboardInterrupt:
            self.http.shutdown()

    def makeHandler(self, request, client_address, connection_handler):
        return RequestHandler(self, request, client_address, connection_handler)

    def create_dom(self):
        DOM().do_render()
