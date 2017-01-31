import pygame
from wall import Wall
from player import Player
from enemy import Enemy
from enemy_hori import EnemyHori
from goal import Goal
from bomb import Bomb
from cracked_wall import Cracked_Wall
from enemy_vert import EnemyVert
from bullet import Bullet
from enmy_shoot_cross import EnemyShooterCross
import time
from enmy_charger import EnemyCharger
from level import Level
from camera import Camera
from explosion import Explosion
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0,0,255)
brown = (160,82,45)
gold = (255,215,0)
green = (0,128,0)
display_width = 800
display_height = 600
tan = (210,180,140)

gameDisplay = pygame.display.set_mode((display_width, display_height))  # surface object
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()
FPS = 20

bomb_img = pygame.image.load('bomb.png')
brick_wall_img = pygame.image.load('brick_wall_1.png')
brick_wall__crack_img = pygame.image.load("brick_wall_cracked_1.png")
explosion_sheet = pygame.image.load("explosion_sprite_sheet.png")

numImages = 10
cur_image= 0
font = pygame.font.SysFont(None, 25)
#player = Player(display_width,display_height)

pygame.key.set_repeat(1,30) # sets the interval and delay when holding down keys

enemy = Enemy(140,40)



def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])  # puts font on bomber display


# def place_bomb(bomb_list):
#     """Adds a bomb to a list of bombs that are not primed"""
#     bomb_list.append(pygame.Rect([player.get_player_posx(), player.get_player_posy(), player.get_player_size(), player.get_player_size()]))
#
# def prime_bomb(bomb_list,primed_bomb_queue,bomb_expl_queue):
#     """Starts the countdown for a bomb to explode"""
#     if bomb_list != []:  # bomb list allows me to start the timer only once per bomb. bomb is moved to primed_bomb_queue
#         # After the certain amount of seconds, the bomb is removed from the bomb_expl_queue
#         t = Timer(4, explode_bomb, [primed_bomb_queue, bomb_expl_queue])
#         t.start()
#         primed_bomb_queue.append(bomb_list.pop())

def display_primed_bomb(primed_bomb_queue):
    """for every bomb that hasn't exploded, it is displayed here"""
    for bomb in primed_bomb_queue:


        gameDisplay.blit(bomb_img, (bomb[0], bomb[1]))
        #gameDisplay.blit(bomb_img, (camera.apply(bomb)))
        pygame.display.update()

# def explode_bomb(primed_bomb_queue, bomb_expl_queue):
#     """Bomb explodes by removing it from the bomb_expl_queue. After a set amount of time, the explosion is removed
#     from the explosion queue and goes away"""
#     bomb_expl_queue.append(primed_bomb_queue.pop(0))
#     t = Timer(.5, bomb_expl_queue.pop, [0])
#     t.start()


def gameLoop(level): # allows for separate handling of exit bomber and bomber over

    gameExit = False
    gameOver = False
    win = False

    time1 = time.time()

    bomb_list = []
    primed_bomb_queue = []
    bomb_expl_queue = []
    wall_list = []
    bullet_list = []
    enemy_list = []
    x = 0
    y = 0

    for row in level.load_lvl():

        for col in row:
            if col == "W":  # denotes a wall
                #print(x)
                wall_list.append(Wall(x, y, 15))  # stores a list of all walls
            elif col =="H":  # denotes an enemy that moves horizontally
                enemy_list.append(EnemyHori(x,y))
            elif col == "V":
                enemy_list.append(EnemyVert(x,y))
            elif col == "G":
                goal = Goal(x,y)
            elif col == "P":
                player = Player(x,y)
            elif col == "C":
                wall_list.append(Cracked_Wall(x,y,15))
                #crack_wall_list.append(Cracked_Wall(x, y, 15))
            elif col == "B":
                bullet_list.append(Bullet(x,y,"west"))
            elif col == "+":
                enemy_list.append(EnemyShooterCross(x,y))
            elif col == "c":
                enemy_list.append(EnemyCharger(x,y))
            x += 15
        y += 15
        x = 0
    #camera = Camera(level.get_map_width(), level.get_map_height(), display_width, display_height)

    while not gameExit:  # event handler
        #if pygame.key.get_repeat() != (1,30):
         #   pygame.key.set_repeat(1,30)
        pygame.event.pump()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameExit = True
                    win = False

        while gameOver == True:

            message_to_screen("Game over, press C to continue or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:  # restart bomber
                        print("hi")
                        gameOver = False
                        pygame.event.clear()
                        gameLoop(level)
        while win == True:
            message_to_screen("You win! Press C to play again or Q to quit", green)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:

                        gameExit = True
                        win = False

                    if event.key == pygame.K_c:  # restart bomber
                        win = False
                        level.next_lvl()
                        gameLoop(level)


        #keys = pygame.key.get_pressed()  # checking pressed keys


        #controls player movement
        player.get_key_press(wall_list,bomb_list,primed_bomb_queue, bomb_expl_queue)



        #bullet behavior
        for bullet in bullet_list:
            bullet.move(bullet_list,wall_list)


        # enemy behavior
        for enemy in enemy_list:
            time2 = time.time()
            elaspe_time = time2 - time1
            if type (enemy) is EnemyCharger:
                enemy.move(wall_list,player,elaspe_time)
            elif type(enemy) is not EnemyShooterCross:
                enemy.move(wall_list)
            if enemy.touch_explosion(bomb_expl_queue):
                enemy_list.remove(enemy)

        for enemy in enemy_list:
            time2 = time.time()
            elaspe_time = time2-time1
            if type(enemy) is EnemyShooterCross:
                #print (elaspe_time%3)
                # this controls how fast the bullets are fired. Lower the mod, the faster the rate of fire
                # changed bounds to control number of bullets fired at once
                if (elaspe_time)%2 >=1 and elaspe_time%2 < 1.15 :
                # t = Timer(.5, enemy.shoot, [bullet_list])
                # t.start()
                    enemy.shoot(bullet_list)


        # Game Over and level end conditions
        if player.touch_explosion(bomb_expl_queue):
            gameOver = True
        if player.touch_enemy(enemy_list) and player.player_health <0:
            gameOver = True
        if player.touch_bullet(bullet_list) and player.player_health <0:
            gameOver = True
        if player.touch_goal(goal):
            win = True


        for wall in wall_list:
            if type(wall) is Cracked_Wall:
                if wall.touch_explosion(bomb_expl_queue):

                    wall_list.remove(wall)


        # Render things

        gameDisplay.fill(white)  # can use to clear stuff


        for wall in wall_list:
            if type(wall) is Cracked_Wall:
                gameDisplay.blit(brick_wall__crack_img,(wall.get_xpos(), wall.get_ypos()))
                #gameDisplay.blit(brick_wall__crack_img, (camera.apply(wall)))

            #gameDisplay.fill(wall.get_color(), rect=wall.rect)
            else:
                gameDisplay.blit(brick_wall_img,(wall.get_xpos(),wall.get_ypos()))
                #gameDisplay.blit(brick_wall_img,(camera.apply(wall)))


        display_primed_bomb(primed_bomb_queue)


        for enemy in enemy_list:
            if type(enemy) is EnemyCharger:
                enemy.sight(gameDisplay)
            #gameDisplay.fill(enemy.get_color(), rect=enemy.rect)
            #gameDisplay.blit(enemy.image,camera.apply(enemy))
        for bullet in bullet_list:

            gameDisplay.fill(bullet.get_color(), rect=bullet.rect)
            print(gameDisplay.fill(bullet.get_color(), rect=bullet.rect))
        gameDisplay.fill(goal.get_color(), rect=goal.rect)
        #gameDisplay.fill(blue, rect=player.rect)  # where we draw guy. superior way of drawing rectangles
        gameDisplay.blit(player.image,(player.get_player_posx(),player.get_player_posy()))

        for explosion in bomb_expl_queue:
            explosion.display_explosion(bomb_expl_queue,gameDisplay)
        player.draw_health(gameDisplay)
        #camera.update(player)
        pygame.display.update()


        clock.tick(FPS)

    pygame.quit()
    quit()

level = Level()
gameLoop(level)