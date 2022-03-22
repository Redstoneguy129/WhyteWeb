class Component:
    def __init__(self, props, *children):
        self.props = props[0]
        self.children = children

    def on_update(self):
        return ()

    def on_render(self):
        return None
