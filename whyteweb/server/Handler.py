from http.server import BaseHTTPRequestHandler
from html.parser import HTMLParser as htmlParser

from whyteweb.client import Component


class HTMLParser(htmlParser):
    def __init__(self, data):
        super().__init__()
        self.data = self.BigData()
        self.feed(data)
        print(self.data.tree)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.data.add_key(tag)
        for at in attrs:
            self.data.add_attribute(at)
        self.data.become_child(tag)

    def handle_endtag(self, tag: str) -> None:
        self.data.become_parent()

    class BigData:
        def __init__(self):
            self.tree = {}
            self.placement = []

        def become_child(self, key):
            self.placement.append(key)

        def get_parent(self, key):
            return self.placement[self.placement.index(key)-1]

        def become_parent(self):
            self.placement.pop()

        def add_key(self, key):
            path = self.placement + [key]
            print(path)
            self.tree[key] = {}
            #if self.level not in self.tree:
            #    self.tree[self.level] = {}
            #self.tree[self.level]["key"] = key

        def add_attribute(self, attribute):
            pass
            #if "attributes" not in self.tree[self.level]:
            #    self.tree[self.level]["attributes"] = []
            #self.tree[self.level]["attributes"].append([attribute[0], attribute[1]])


class RequestHandler(BaseHTTPRequestHandler):

    def __init__(self, serve, *args, **kwargs):
        self.parent = serve
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path in self.parent.get_router().get_paths():
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(self.parent.get_router().get_route(self.path).value, "utf-8"))
        else:
            self.send_response(404)
            self.end_headers()


class DOM:
    def __int__(self, app: Component):
        self.app = app

    @staticmethod
    def get_template():
        return """
        <html>
            <head>
                <meta charset="utf-8"/>
            </head>
            <body id="root"></div>
        </html>
        """

    def do_render(self):
        template = self.get_template()
        HTMLParser(template)
