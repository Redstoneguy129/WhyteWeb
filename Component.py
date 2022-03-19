class Component:
    def __init__(self, props, *children):
        self.props = props[0]
        self.children = children
    def onUpdate(self):
        return ()
    def render(self):
        return None
