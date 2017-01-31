import pygame
class Goal:

    def __init__(self,xpos,ypos):
        self.size = 15
        self.rect = pygame.Rect(xpos, ypos, self.size, self.size)
        self.color = (255,215,0)

    def get_color(self):
        return self.color

