#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400                #creating a screen 
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0           #counter of points

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r'C:\Users\Assan\OneDrive\Desktop\PP2\AnimatedStreet.png')

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):              ##Create an enemy
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'C:\Users\Assan\OneDrive\Desktop\PP2\Enemy.png')  ## picture of enemies' cars
        self.rect = self.image.get_rect()               #creating a rectangle as the surface of an object 
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):                 #machine movement function 
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):             ##creating a player
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'C:\Users\Assan\OneDrive\Desktop\PP2\Player.png') ##Loading picture of player car
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()              #a variable that will accept keystrokes on the keyboard
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:        
                  self.rect.move_ip(-5, 0)              #moving the object up the specified number of steps vertically
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):           ## creating coins
    def __init__(self): 
        super().__init__() 
        self.surf =pygame.Surface((20, 20)) 
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH - 40), -100)) #the appearance of objects outside the screen 
        self.speed = random.randint(3, 5)           #random speed in the specified range 
        self.random_number = random.randint(0, 3) 
        self.image = pygame.image.load(r'C:\Users\Assan\OneDrive\Desktop\PP2\tenge.png') ##image of coin
      
 
    def move(self): 
        self.rect.move_ip(0, self.speed) 
 
    def draw(self): 
        self.surf.blit(pygame.transform.scale(self.image, (20, 20)), (0, 0)) 
        DISPLAYSURF.blit(self.surf, (self.rect.x, self.rect.y)) 
 
    def death(self): 
        if self.rect.top > SCREEN_HEIGHT: 
            self.kill() 
                  

#Setting up Sprites        
P1 = Player()           #assigning a class to a variable 
E1 = Enemy()
coins = pygame.sprite.Group()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins.add(coins)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coins)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:      #when the screen is closed, the cycle stops
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)       #displaying the number of points on the screen 
    DISPLAYSURF.blit(scores, (10,10))

    for coin in coins: 
        coin.draw()
        coin.move() 
        coin.death() 

    for coin in pygame.sprite.spritecollide(P1, coins, True): 
        SCORE += 1                                          #increasing the number of points 
      
        

    if coins.__len__() < 2: 
        coins.add(Coin())


    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r'C:\Users\Assan\OneDrive\Desktop\PP2\crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()          #updating the screen with changes 
    FramePerSec.tick(FPS)