import pygame


class Wall:

    def __init__(self, pos_x, pos_y,size):
        global walls
        #blue = (0, 0, 255)
        self.color = (160,82,45)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size
        self.rect = pygame.Rect(self.pos_x,self.pos_y,self.size, self.size)



    def get_color(self):
        return self.color
    def get_xpos(self):
        return self.pos_x
    def get_ypos(self):
        return self.pos_y


