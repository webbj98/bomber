import pygame
class Enemy:

    def __init__(self, xpos, ypos):
        self.size = 15
        self.rect = pygame.Rect(xpos,ypos, self.size,self.size)
        self.face_dir = "west"
        self.steps = 0
        self.image = pygame.image.load("enemy_temp.png")
        self.pos = (xpos,ypos)

    def change_dir(self,direction):
        """Changes the direction the enemy is facing. Uses words like north and south"""
        self.face_dir = direction

    def change_steps(self, num):
        """
        Changes the number of steps based on value passed. Steps are used to time
        how long the enemy will go in a direction before turning around.
        """
        self.steps += num

    def get_size(self):
        return self.size

    def touch_explosion(self,bomb_expl_queue):
        """Check if player is touching an explosion and returns true or false"""
        for explosion in bomb_expl_queue:
            #print (self.rect.colliderect(explosion))
            #print ("hi")
            if self.rect.colliderect(explosion):
                return True
    def get_pos(self):
        return self.pos