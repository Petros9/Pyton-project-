from src.basic.point import Point


class Spawn:
    def __init__(self, x=40, y=20):
        self.position = Point(x, y)

    def change_spawn(self, x, y):
        self.position = Point(x, y)
