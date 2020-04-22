from basic.point import Point
from basic.direction import Direction
from world_elements.spawn import Spawn
from physics_object import PhysicsObject


class Hero(PhysicsObject):
    def __init__(self, level):
        self.spawn = Spawn()
        super().__init__(self.spawn.position)
        self.position = self.spawn.position
        self.health = 10
        self.direct = Direction.RIGHT
        self.level = level
        self.assign_world(level)
        self.squat = False
        self.shooting = False

    def move_position(self, dx, dy):
        new_position = self.position + Point(dx, dy)
        if (self.can_move_to(new_position)):
            self.position = new_position

    def can_move_to(self, point):
        return self.level.object_at(point) is False

    def left_direction(self):
        self.direct = Direction.LEFT

    def right_direction(self):
        self.direct = Direction.RIGHT

    def is_in_right_direction(self):
        return self.direct == Direction.RIGHT

    def take_hit(self):
        self.health -= 2

    def change_squat_state(self):
        self.squat = not self.squat

    def shoot(self):
        if(self.is_in_right_direction()):
            self.level.shoot(self.position.x+6, self.position.y, 3)
        else:
            self.level.shoot(self.position.x-6, self.position.y, -3)


