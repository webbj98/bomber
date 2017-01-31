import pygame
from enemy import Enemy
from bullet import Bullet
from threading import Timer
from player import Player
class EnemyCharger(Enemy):
    """This enemies, upon seeing the player, charges in a straight line at them"""

    def __init__(self,xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (255,165,0)  # orange
        self.vis_color = (0,0,255)  # blue
        self.vis_color1 = (255,0,0) # red
        self.vis_size = 250

        Enemy.__init__(self,xpos,ypos)
        self.size =20
        self.rect = pygame.Rect(xpos, ypos, self.get_size(), self.get_size())

        self.vision_xpos = self.rect.x
        self.face_dir = "north"
        self.vision =  pygame.Rect((self.rect.x-int((self.get_vision_size()-self.get_size())/2),self.rect.y -int((self.get_vision_size()-self.get_size())/2),self.get_vision_size(),self.get_vision_size()))
        self.is_charging = False
        self.trajx = 0
        self.trajy = 0
        self.steps =15  # controls how long it will take for enemy to charge to location
        self.can_charge = True
        self.image = pygame.image.load("charger_temp.png")
    def get_color(self):
        if self.can_charge == False:
            return (255, 127,80) # coral
        else:
            return self.color

    def sight(self,surface):
        # pygame.draw.circle(surface, self.vis_color, (self.rect.x + int(.5 * self.get_size() )
        #                                      , int(self.rect.y + .5 * self.get_size())),
        #                   self.get_vision_radius() , 0)
        #pygame.draw.rect(surface, self.vis_color1, (self.vision), 0)
        x = 0


    def move_single_axis(self,dx,dy,walls):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
        self.vision.y -= self.trajy
        self.vision.x -= self.trajx

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            #print (type(wall))
            #print("dx " + str(dx))
            #print("dy " + str(dy))
            if self.rect.colliderect(wall.rect) :


                if dx > 0:  # Moving right; Hit the left side of the wall

                    self.rect.right =wall.rect.left
                    self.vision.right = abs(wall.rect.left + self.get_vision_size()/2)
                    #print("you hit wall")
                if dx < 0:  # Moving left; Hit the right side of the wall
                    if self.vision.x < 0:  # prevents the vision rectangle from not moving outside the screen
                        self.vision.x = self.vision.x
                        #print ("less than zero")
                    else:
                        self.vision.left = abs(wall.rect.right - self.get_vision_size() / 2 )
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom  =wall.rect.top
                    self.vision.bottom = abs(wall.rect.top+ self.get_vision_size() / 2)
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    if self.vision.y < 0: # prevents the vision rectangle from not moving outside the screen
                        self.vision.y = self.vision.y
                    else:
                        self.vision.top = abs(wall.rect.bottom - self.get_vision_size() / 2)
                    self.rect.top = wall.rect.bottom
                self.set_is_charging(False)
                self.set_can_charge(False)
                dx = 0
                dy =0
                timer = Timer(2, self.set_can_charge, [True])
                timer.start()


    def move(self, wall_list,player, time_elasped):
        if self.vision.colliderect(player) and self.is_charging == False and self.can_charge:
            self.set_is_charging(True)
            # determines direction for enemy to charge
            self.trajx = ((self.rect.x - player.get_player_posx())//self.steps)
            self.trajy = ((self.rect.y - player.get_player_posy())//self.steps)
            #print (self.trajx)
            #print (self.trajy)
        if self.is_charging:

            #self.rect.x -= self.trajx
            #self.rect.y -= self.trajy

            self.move_single_axis( -self.trajx,-self.trajy , wall_list)


    def get_vision_size(self):
        return self.vis_size

    def set_vision_size(self,x,y):
        return
    def get_size(self):
        return self.size

    def set_is_charging(self, bool):
        self.is_charging = bool
    def set_can_charge(self,bool):
        self.can_charge = bool


