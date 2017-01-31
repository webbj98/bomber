import pygame
from threading import Timer
from explosion import Explosion
class Bomb:
    def __init__(self,xpos,ypos,size):
        self.timer = 3
        self.size = 15
        self.xpos = xpos
        self.ypos = ypos
        self.rect = pygame.Rect(self.get_xpos(), self.get_ypos(), self.size, self.size)

        self.cur_image = 0
        self.num_images = 10
        self.explosion_sheet = pygame.image.load("explosion_sprite_sheet.png")

    def place_bomb(self,bomb_list):
        """Adds a bomb to a list of bombs that are not primed"""
        bomb_list.append(self.rect)

    def prime_bomb(self, bomb_list, primed_bomb_queue, bomb_expl_queue):
        """Starts the countdown for a bomb to explode"""
        if bomb_list != []:  # bomb list allows me to start the timer only once per bomb. bomb is moved to primed_bomb_queue
            # After the certain amount of seconds, the bomb is removed from the bomb_expl_queue
            t = Timer(2, self.explode_bomb, [primed_bomb_queue, bomb_expl_queue])
            t.start()
            primed_bomb_queue.append(bomb_list.pop())

    def explode_bomb(self,primed_bomb_queue, bomb_expl_queue):
        """Bomb explodes by removing it from the bomb_expl_queue. After a set amount of time, the explosion is removed
        from the explosion queue and goes away"""
        exp_bomb = primed_bomb_queue.pop(0)
        bomb_expl_queue.append(Explosion(exp_bomb[0], exp_bomb[1], self.size))
        t = Timer(.5, bomb_expl_queue.pop, [0])
        t.start()

    def get_xpos(self):
        return self.xpos
    def get_ypos(self):
        return self.ypos

    # def display_explosion(self,bomb_expl_queue, gameDisplay):
    #
    #     for explosion in bomb_expl_queue:
    #         gameDisplay.blit(self.explosion_sheet, (explosion.get_xpos(), explosion.get_ypos()),
    #                          (self.cur_image * 19, 0, explosion.get_size(), explosion.get_size()))
    #         # pygame.draw.circle(gameDisplay,red,(explosion.get_xpos()+int(.5*explosion.get_size())
    #         #                                     ,int(explosion.get_ypos()+.5*explosion.get_size())),explosion.get_size()-1,0)
    #
    #         # gameDisplay.fill(gold, rect = explosion)  shows the actual explosion rectangle
    #         self.curr_image +=1
    #         pygame.display.update()
