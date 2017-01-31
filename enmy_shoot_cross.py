import pygame
from enemy import Enemy
from bullet import Bullet
from threading import Timer

class EnemyShooterCross(Enemy):
    """This enemies fires bullets in a cross pattern"""
    def __init__(self,xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (119,136,153)  # slate gray
        Enemy.__init__(self,xpos,ypos)
        self.rect = pygame.Rect(xpos, ypos, self.get_size(), self.get_size())
        self.face_dir = "north"
        self.can_shoot = True

    def get_color(self):
        return self.color

    def shoot(self,bullet_list):
        #
        bullet_list.append(Bullet(self.xpos, self.ypos, "north",self.get_size()))
        bullet_list.append(Bullet(self.xpos, self.ypos, "south",self.get_size()))
        bullet_list.append(Bullet(self.xpos, self.ypos, "east", self.get_size()))
        bullet_list.append(Bullet(self.xpos, self.ypos, "west", self.get_size()))


