import pygame
import random
from os import path
difficulty = 0
difficultyS = input("Enter a difficulty.")
if difficultyS == (""):
    difficultyS = input("You failed to enter a difficulty. Enter a difficulty.")
    
difficulty = difficultyS
difficulty = int(difficulty)

killCount = 0

pygame.display.set_caption('font example')
size = [640, 480]

width = 1000
height = 1000
fps = 60

#Colours
rand = random.random()
rand1 = random.random()
rand2 = random.random()
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0 ,0)
Lime = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Cyan = (0,255,255)
Magenta = (255,0,255)
Silver = (192,192,192)
Grey = 	(128,128,128)
Maroon = (128,0,0)
Olive = (128,128,0)
Green = (0,128,0)
Purple =(128,0,128)
Teal = (0,128,128)
Navy = (0,0,128)
transparentBlue = (0, 0, 255, 1)

pygame.init()
pygame.mixer.init() #sound
pygame.mixer.music.load('rickroll.mp3')
pygame.mixer.music.play(0)
screen = pygame.display.set_mode((width, height)) #create screen
pygame.display.set_caption("NAME") #give game name
clock = pygame.time.Clock() #fps count

img_dir = path.join(path.dirname(__file__), "Anything you want")
player_img = pygame.image.load(path.join(img_dir, "Player.png")).convert()
mob_img = pygame.image.load(path.join(img_dir, "Meteor.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "Laser.png")).convert()
enemy_img = pygame.image.load(path.join(img_dir, "Enemy.png")).convert()

font_name = pygame.font.match_font("Arial")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, Black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.center = (10, 100)
        self.speedx = -1
    def update(self):
        self.rect.x += self.speedx
    """def shoot(self):
        bullet = Bullet(self.rect.centerx - 50, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootr(self):
        bullet = Bullet(self.rect.centerx + 50, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)"""

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height-100)

    def update(self):
        pressed = pygame.key.get_pressed()  
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.rect.x += 5 
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.rect.x -= 5
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            self.rect.y += 5
        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.rect.y -= 5
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.bottom < 0:
            self.rect.bottom = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx - 50, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootr(self):
        bullet = Bullet(self.rect.centerx + 50, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(Black)
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(4, 10)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > height + 10:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(4, 10)
            self.speedx = random.randrange(-3, 3)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y ):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        pressed = pygame.key.get_pressed()
        if self.rect.bottom < 0:
            self.kill

bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
for i in range (difficulty):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)
enemies = pygame.sprite.Group()
for i in range (1):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
#Game loop
running = True
while running:

    clock.tick(fps)
 #keep loop running at the right speed
    #process inputs,
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                player.shootr()
     
    #updates,
    all_sprites.update()
    randomColour = (rand * 255, rand1 * 255, rand2 * 255)
    rand = random.random()
    rand1 = random.random()
    rand2 = random.random()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        mob = Mob()
        all_sprites.add(mob)
        mobs.add(mob)
        killCount+=1
        draw_text()
        
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
    #renders
    screen.fill(randomColour)
    all_sprites.draw(screen)
    draw_text(screen, ("Score: " + str(killCount)), 20, width/2, 10)
    #after drawing, flip the display
    pygame.display.flip()
pygame.quit()
    
