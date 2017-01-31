import pygame

class Bullet:

    def __init__(self, xpos, ypos, direction, emmiter_size):
        self.direction = direction
       # self.direction2 = direction2
        self.xpos = xpos+ emmiter_size//2
        self.ypos = ypos +emmiter_size//2
        self.size = 5
        self.color = (192,192,192)  # silver
        self.rect = pygame.Rect(self.xpos, self.ypos, self.get_size(), self.get_size())


    def move(self,bullet_list,wall_list):
        """
        Moves the bullet based on the direction they were fired from.
        Will stop when it hits a wall
        """
        if self.touch_wall(wall_list):

            bullet_list.remove(self)

        elif self.direction ==  "north":
            self.rect.x -=7
        elif self.direction  == "south":
            self.rect.x +=7
        elif self.direction == "east":
            self.rect.y +=7
        elif self.direction == "west":
            self.rect.y -= 7



        #self.rect.x +=1
    def touch_wall(self,wall_list):
        """Check if cracked wall is touching an explosion and returns true or false"""
        for wall in wall_list:
            if self.rect.colliderect(wall):
                return True
    def get_xpos(self):
        return self.xpos

    def get_ypos(self):
        return self.ypos

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size