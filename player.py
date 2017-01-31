import pygame
from wall import Wall
from bomb import Bomb
from threading import Timer
class Player:
    green = (124, 252, 0)
    def __init__(self, xpos, ypos):

        self.player_size = 15
        self.player_x_change = 0
        self.player_y_change = 0
        self.rect = pygame.Rect(xpos, ypos , 15, 15)
        self.can_place_bomb = True
        self.player_health = 3
        self.image = pygame.image.load("player_temp.png")


    #bug has something to do with walls probably
    def move_single_axis(self, dx, dy,walls):

        # Move the rect

        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            #print (type(wall))
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall

                    self.rect.right = wall.rect.left
                    #print("you hit wall")
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    #print ("you hit wall")
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

    def get_key_press(self,walls,bomb_list,primed_bomb_queue, bomb_expl_queue):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.move(-5,0,walls)
        if keys[pygame.K_RIGHT]:
            self.move(5, 0, walls)
        if keys[pygame.K_UP]:
            self.move(0, -5, walls)
        if keys[pygame.K_DOWN]:
            self.move(0,5,walls)
        if keys[pygame.K_SPACE] and self.can_place_bomb== True:
            bomb = Bomb(self.get_player_posx(), self.get_player_posy(), 15)
            bomb.place_bomb(bomb_list)
            bomb.prime_bomb(bomb_list, primed_bomb_queue, bomb_expl_queue)
            self.set_can_place_bomb(False)
            timer = Timer(.5, self.set_can_place_bomb, [True])
            timer.start()
            print (self.can_place_bomb)


    def move(self, dx, dy,walls):
    # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:

            self.move_single_axis(dx, 0,walls)
        if dy != 0:
            self.move_single_axis(0, dy,walls)
    def get_player_posx(self):
        """returns the player's x pos as an integer"""

        return self.rect.x

    def get_player_posy(self):
        """returns the player's y pos as an integer"""
        return self.rect.y

    def get_player_size(self):
        """returns the player's size as an interger"""
        return self.player_size

    def touch_explosion(self,bomb_expl_queue):
        """Check if player is touching an explosion and returns true or false"""
        for explosion in bomb_expl_queue:
            #print (self.rect.colliderect(explosion))
            #print ("hi")
            if self.rect.colliderect(explosion):
                return True

    def touch_enemy(self,enemy_list):
        """Checks if a player is touching an enemy and returns true or false"""
        for enemy in enemy_list:
            if self.rect.colliderect(enemy):
                self.player_health -=1
                return True

    def touch_goal(self,goal):
        """Checks if a player is touching an enemy and returns true or false"""
        if self.rect.colliderect(goal):
            return True

    def touch_bullet(self,bullet_list):
        """Checks if a player is touching a bullet. If so, returns true"""
        for bullet in bullet_list:
            if self.rect.colliderect(bullet):
                self.player_health -=1
                return True

    def set_can_place_bomb(self,bool):
        self.can_place_bomb = bool

    def draw_health(self,gameDisplay):
        if self.player_health > 1:
            col = (124, 252, 0) #light green
        else:
            col = (255,0,0) # red
        width = int(50*self.player_health/3)
        self.health_bar = pygame.Rect(50,0, width,10)
        #if self.player_health <4:
        pygame.draw.rect(gameDisplay,col, self.health_bar)
        #gameDisplay.fill(col,rect= self.health_bar)
        pygame.display.update()