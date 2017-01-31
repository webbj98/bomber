import pygame

class Explosion:
    def __init__(self,xpos, ypos, size):
        self.radius_mod = 12   # determines the additional radius of the explosion
        self.xpos = xpos - self.radius_mod//2
        self.ypos = ypos - self.radius_mod//2
        self.size = size + self.radius_mod
        self.rect = pygame.Rect(self.xpos, self.ypos, self.size, self.size)

        self.explosion_sheet = pygame.image.load("explosion_sprite_sheet_resized.png")
        self.curr_image=0
        self.num_images = 10

    def display_explosion(self, bomb_expl_queue,gameDisplay):
        #gameDisplay.fill((255, 215, 0), rect=self)  # shows the actual explosion rectangle
        gameDisplay.blit(self.explosion_sheet, (self.get_xpos(), self.get_ypos()),
        (self.curr_image * 26, 0, self.get_size(), self.get_size()))

        # pygame.draw.circle(gameDisplay,red,(explosion.get_xpos()+int(.5*explosion.get_size())
        #                                     ,int(explosion.get_ypos()+.5*explosion.get_size())),explosion.get_size()-1,0)


        self.curr_image +=1
        #pygame.display.update()
    def get_xpos(self):
        return self.xpos
    def get_ypos(self):
        return self.ypos
    def get_size(self):
        return self.size