import pygame
from enemy import Enemy

class EnemyVert(Enemy):
    def __init__(self,xpos, ypos):
        self.color = (119,136,153)  # slate gray
        Enemy.__init__(self,xpos,ypos)
        self.rect = pygame.Rect(xpos, ypos, self.get_size(), self.get_size())
        self.face_dir = "north"


    def get_color(self):
        return self.color

    def move_single_axis(self,dy,walls):

        # Move the rect
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            #print (type(wall))
            if self.rect.colliderect(wall.rect):
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    self.change_dir("north")
                    self.steps = 0
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    self.change_dir("south")
                    self.steps = 0
    def move(self, wall_list):

        """
        Moves the enemy in a predetermined direction

        This enemy moves Horizontal
        """
        if self.steps != 40:

            if self.face_dir == "north":
                self.move_single_axis(-3, wall_list)
                #self.rect.y -= 3
            if self.face_dir == "south":
                self.move_single_axis(3, wall_list)
                #self.rect.y += 3
        else:

            if self.face_dir == "north":
                self.change_dir("south")
            elif self.face_dir == "south":
                self.change_dir("north")
            self.steps = 0
        self.change_steps(1)