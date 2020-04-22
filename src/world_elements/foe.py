from src.basic.point import Point


class Foe:
    def __init__(self, x, y):
        self.position = Point(x, y)
        self.foe_health = 3
        self.foe_direct = -1  # '' może lepiej zrobić enum left i right, choć
        # '' w sumie w pythonie enumy nie maja
        # '' az takiej mocy

    def move(self, new_direct=-1):
        self.foe_direct = new_direct
        # os x
        shift = Point(self.foe_direct, 0)
        self.position += shift

    def take_hit(self):
        self.foe_health -= 10

    def position_on_screen(self, hero_position):
        return self.position.x - hero_position + 30