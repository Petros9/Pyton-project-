"""from direction import Direction

### to możnaby trochę zmienić, żeby było bardziej pythonowe
### (ale jeszcze nwm jak)
class Spawn:

    def __init__(self, x, y):
        self.spawn_point = Point(x, y)

    def set_new_spawn(self, new_x, new_y):
        self.x_start_position = new_x
        self.y_start_postion = new_y

    def get_spawn_point(self):
        return self.spawn_point


class Hero:

    def __init__(self):
        self.spawn = Spawn()
        self.hero_position = self.spawn.get_spawn_point()
        self.hero_health = 10
        self.hero_direct = Direction.RIGHT
        self.hero_jump = 0 # '' daje te opcje, w razie jakichś przyszłych
        # '' animacji

    def move_position(self, new_direct = Direction.RIGHT, new_jump = 0):
        self.hero_direct = new_direct
        self.hero_jump = new_jump
        shift = Point(self.hero_direct, self.hero_jump)
        #testujemy shitf (czy jakieś obiekty)
        self.hero_position += shift
        # tu zrobić różne warianty:
            #wchodzi na flagę
            #wchodzi na platformę
            #wchodzi na wroga
            #wchodzi na coś innego

class Bullet:
    def __init__(self, x = 0, y = 0, direct = 1):
        self.bullet_position = Point(x,y)
        self.bullet_speed = direct

class World:
    def __init__(self):
        self.hero = Hero()
        self.flagList = list()
        self.mapa = dict()
    def object_at(self,point):
        return False
        



class Flag:
    def __init__(self, x = 0, y = 0):
        self.flag_point = Point(x,y)
        self.active = False
    def place_flag(self, x, y):
        self.flag_point.set_point(x,y)
    def get_flag_point(self):
        return self.flag_point

###klasy:
# - mapa
# - platformy
# - wrogowie
# - wieżyczki
# - ew. zapadnia 

### animacje:
# skok
# ruch (prawo i lewo)
# obrót wieżyczki


### część okienkowa:
# okno startowe
# okno rozgrywki
# okno końca gry
# może jakieś audio nagrać czy coś
# grafika
"""