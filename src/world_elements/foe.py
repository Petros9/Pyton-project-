from basic import Point
from character import Character
import basic as bs
from models import Models
from settings import HORIZONTAL_ACCELERATION, IMMORTALITY_TIME, FOE_BULLETS_PER_BURST, CELL_SIZE, FOE_RANGE


class Foe(Character):
    def __init__(self, img, x, y, level):
        super().__init__(img, bs.Point(x, y), level)
        self.foe_health = 3
        self.foe_direct = bs.Direction.LEFT
        self.immortality_timer = 0
        self.reload_timer = 0
        self.bullets = FOE_BULLETS_PER_BURST

    def take_hit(self):
        self.foe_health -= 1
        self.immortality_timer = IMMORTALITY_TIME
        if(self.foe_direct == bs.Direction.LEFT):
            self.image = Models.FOE_L_DAM_IMG
        else:
            self.image = Models.FOE_R_DAM_IMG

    def shoot(self):
        if (self.foe_direct == bs.Direction.RIGHT):
            bullet_position = Point(self.rect.x + 18, self.rect.y)
            bullet_velocity = Point(15, 0)
            self.world.shoot(bullet_position, bullet_velocity)
        else:
            bullet_position = Point(self.rect.x - 18, self.rect.y)
            bullet_velocity = Point(-15, 0)
            self.world.shoot(bullet_position, bullet_velocity)

    def change_image(self):
        if(self.foe_direct == bs.Direction.RIGHT):
            self.image = Models.FOE_R_IMG
        else:
            self.image = Models.FOE_L_IMG

    def reaches(self, hero_position):
        if(abs(hero_position.y - self.position.y) > CELL_SIZE*3/4):
            return False
        else:
            if(self.foe_direct == bs.Direction.LEFT):
                return self.position.x - hero_position.x < FOE_RANGE
            else:
                return self.position.x - hero_position.x > FOE_RANGE

    def update(self):
        super().update()
        return self.position


