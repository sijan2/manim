from manimlib import *


class HelloWorld(InteractiveScene):
    def construct(self):
        text = Text("Hello")
        self.add(text)
