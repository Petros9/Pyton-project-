from world_elements.hero import Hero
from world_elements.foe import Foe
from world_elements.flag import Flag
from world_elements.bullet import Bullet
from world_elements.platform import Platform
class Level:
    def __init__(self, objects):
        self.hero = Hero(self)
        self.tower_list = []  # '' wiezyczki beda strzelaly w dol co jakiś czas
        self.objects = objects
        self.level_objects = {}
        self.foes_list = []
        self.place_objects(objects)
        self.bullets_list = []

    # '' przesuwanie sie wrgow czyszczenie wrogow itd
    # '' trzeba zrobić, by wrogowie nie spadali z platform

    def object_at(self, point):
        if ((point.x, point.y) in self.level_objects):
            map_object = self.level_objects.get((point.x, point.y))


            if (isinstance(map_object, Flag)):
                self.hero.spawn.change_spawn(point.x, point.y)
                map_object.capture()
                return None
            elif (isinstance(map_object, Foe)):
                self.hero.take_hit()
            #zastanawia mnie zasadnosc
            elif (isinstance(map_object, Bullet)):
                if(not self.hero.squat):
                    self.hero.take_hit()
                    del self.level_objects[map_object]
                    del self.bullet_list[map_object]
                return None
            return map_object
        else:
            return None

    def place_objects(self, objects):
        for object in objects:
            self.level_objects[(object.position.x,
                                object.position.y)] = object
            self.foes_list = list(filter(lambda object : isinstance(object, Foe), objects))

    def shoot(self, x, y, direction):
        bullet = Bullet(x, y, direction)
        self.level_objects[(bullet.position.x, bullet.position.y)] = bullet
        self.bullets_list += [bullet]

    def move_bullets(self):
        for bullet in self.bullets_list:
            bullet.move()
            if(bullet.position.__eq__(self.hero.position)):
                self.hero.take_hit()
                del self.bullet_list[bullet]
            else:
                map_object = self.object_at(bullet.position)
                if(isinstance(map_object, Foe)):
                    map_object.take_hi()
                    del self.bullet_list.[bullet]
                elif(isinstance(map_object, Platform)):
                    print("oap")
                    del self.bullet_list[bullet]

    def move_foes(self):
        for foe in self.foes_list:

            foe.move()



