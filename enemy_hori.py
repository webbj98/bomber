import pygame
from enemy import Enemy

class EnemyHori(Enemy):
    def __init__(self,xpos, ypos):
        self.color = (128,128,128)  # gray
        Enemy.__init__(self,xpos,ypos)
        self.rect = pygame.Rect(xpos, ypos, self.get_size(), self.get_size())


    def get_color(self):
        return self.color

    def move_single_axis(self,dx,walls):

        # Move the rect
        self.rect.x += dx

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            #print (type(wall))
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    self.change_dir("west")
                    self.steps = 0
                    #print("you hit wall")
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    self.change_dir("east")
                    self.steps = 0
                    #print ("you hit wall")

    def move(self,wall_list):

        """
        Moves the enemy in a predetermined direction

        This enemy moves Horizontal
        """
        if self.steps != 40:
            if self.face_dir == "west":
                #self.rect.x -= 3
                self.move_single_axis(-3, wall_list)

            if self.face_dir == "east":
                #self.rect.x += 3
                self.move_single_axis(3, wall_list)

        else:

            if self.face_dir == "west":
                self.change_dir("east")
            elif self.face_dir == "east":
                self.change_dir("west")
            self.steps = 0
        self.change_steps(1)