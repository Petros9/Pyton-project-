from src.basic.point import Point

GRAVITY = 1

AIR_RESISTANCE = 5
FRICTION = 0.8
MOVEMENT_RESISTANCE_X = 1.5
MOVEMENT_RESISTANCE_y = 1
UNIT = 10


class PhysicsObject:

    def __init__(self, position, velocity=None, world=None):
        self.position = position
        self.velocity = Point(0, 0) if (velocity is None) else velocity
        self.world = world if (world is not None) else None
        self.jumping = False

    def accelerate(self, ax, ay):

        floor_level = center(self.position + Point(0, 10))
        if (self.world.object_at(floor_level) is None and ay < 0):
            ay = 0
        self.velocity += 0.5 * Point(MOVEMENT_RESISTANCE_X * ax, MOVEMENT_RESISTANCE_y * ay)
        x_direction = 1 if (self.velocity.x >= 0) else -1
        y_direction = 1 if (self.velocity.y >= 0) else -1
        if (abs(self.velocity.x) > AIR_RESISTANCE):
            self.velocity.x = MOVEMENT_RESISTANCE_X * x_direction
        if (abs(self.velocity.y) > AIR_RESISTANCE):
            self.velocity.y = AIR_RESISTANCE * y_direction

    def move(self):

        vec = Point(self.position.x, self.position.y - 0.3 * UNIT)
        vec = center(vec)
        map_object = self.world.object_at(vec)
        if (self.velocity.y < 0 and map_object is None):
            pass
        self.position += self.velocity
        direction = 1 if (self.velocity.x > 0) else -1
        vec = Point(self.position.x + direction * 0.3 * UNIT, self.position.y)
        vec = center(vec)
        map_object = self.world.object_at(vec)
        if (self.velocity.x and map_object is not None):
            self.position.x = map_object.position.x - direction * UNIT
            self.velocity.x = 0
        vec = Point(self.position.x, self.position.y + 1)
        vec = center(vec)
        map_object = self.world.object_at(vec)
        if (self.velocity.y and map_object is not None):
            self.position.y = map_object.position.y - UNIT
            self.velocity.y = 0
            self.jumping = False
        self.position.x = int(self.position.x)
        self.position.y = int(self.position.y)
            
    def update(self):
        floor_level = center(self.position + Point(0, 5))
        if (self.world.object_at(floor_level) is None):
            self.accelerate(0, GRAVITY)
        else:
            self.velocity.x *= FRICTION
        self.move()

    def assign_world(self, world):
        self.world = world


def center(vector):
    vector = UNIT * Point(int(vector.x / UNIT), int(vector.y / UNIT))
    vector += 0.5 * Point(UNIT, UNIT)
    return vector