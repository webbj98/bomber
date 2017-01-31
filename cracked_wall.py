import pygame
from wall import Wall

class Cracked_Wall(Wall):
    def __init__(self, xpos, ypos, size):
        self.pos_x = xpos
        self.pos_y = ypos
        self.rect = pygame.Rect(xpos, ypos, size, size)
        self.color = (210, 180, 140)  # tan
    def touch_explosion(self,bomb_expl_queue):
        """Check if cracked wall is touching an explosion and returns true or false"""
        for explosion in bomb_expl_queue:
            if self.rect.colliderect(explosion):
                return True