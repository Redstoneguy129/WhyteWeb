from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

class Router:
    def __init__(self):
        self.routes = []
    def add_route(self, route):
        self.routes += [route]
    def add_routes(self, routes):
        self.routes += routes
    def remove_route(self, route):
        self.routes.remove(route)
    def remove_routes(self, routes):
        self.routes = [route for route in self.routes if route not in routes]
    def get_path(self, route):
        return self.routes.index(route).path
    def get_paths(self):
        return [route.path for route in self.routes]
    def get_route(self, path):
        return self.routes[self.get_paths().index(path)]
    def get_routes(self):
        return self.routes

class Serve:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.router = Router()
    def __enter__(self):
        parent = self
        self.http = HTTPServer((self.host, self.port), self.makeHandler)
        self.daemon = Thread(target=self.http.serve_forever)
        self.daemon.daemon = True
        return self
    def __exit__(self, type, value, traceback):
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
        except:
            parent = self
            self.http = HTTPServer((self.host, self.port), self.makeHandler)
            self.daemon = Thread(target=self.http.serve_forever)
            self.daemon.start()
        try:
            while True:
                if not self.daemon.is_alive():
                    return
        except:
            self.http.shutdown()
    def makeHandler(self, request, client_address, connection_handler):
        return self.RequestHandler(self, request, client_address, connection_handler)
    class RequestHandler(BaseHTTPRequestHandler):
        parent = None
        def __init__(self, serve, *args, **kwargs):
            global parent
            parent = serve
            super().__init__(*args, **kwargs)
        def do_GET(self):
            global parent
            if self.path in parent.get_router().get_paths():
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes(parent.get_router().get_route(self.path).value, "utf-8"))
            else:
                self.send_response(404)
                self.end_headers()
