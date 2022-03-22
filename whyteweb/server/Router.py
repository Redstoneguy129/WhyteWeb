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
