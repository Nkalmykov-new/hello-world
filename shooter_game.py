#Создай собственный Шутер!
from pygame import *
from random import randint


window = display.set_mode((700, 500))
display.set_caption("Шутер")
#задай фон сцены
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
#создай 2 спрайта и размести их на сцене

clock = time.Clock()
FPS = 60   
x1 = 450
x2 = 550
y1 = 500
vector = 'right'
fall = 'down'
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound("fire.ogg")

n = 0
lost = 0
font.init()
font = font.SysFont('Times New Roman', 50)
Score = font.render('Счетчик: 0', True, (255,250,255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.player_image = player_image
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and player1.rect.x > 5:
            player1.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and player1.rect.x < 690:
            player1.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 5, 20, 20)
        bullets.add(bullet)    
        
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            bullet.kill()

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        global lost    
        if self.rect.y >= 500:
            self.rect.x = randint(50,650)
            self.rect.y = 0  
            lost = lost + 1 
         
player1 = Player('rocket.png', 100, 425, 5, 50, 50)
bullet = Bullet('bullet.png', player1.rect.centerx, player1.rect.top, 5, 20, 20)

ufos = sprite.Group()
bullets = sprite.Group()

for i in range(5):
    ufo = Enemy('ufo.png', randint(50,650), 0, randint(1,3), 40, 40)
    ufos.add(ufo)

flag = True
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if flag == True:
                if e.key == K_SPACE:
                    player1.fire()
                    fire.play()

                    
    if finish != True:
        window.blit(background,(0,0))
    window.blit(Score, (50,50))
    falls = font.render('Пропущено:'+ str(lost), True, (255,250,255))
    window.blit(falls, (50,100))

    if lost >= 3 or sprite.spritecollide(player1, ufos, True):
        finish = True
        game = False

    player1.reset()
    player1.update()

    ufos.update() 
    ufos.draw(window)

    bullet.reset()
    bullet.update()
    bullets.update()
    bullets.draw(window)
    
    if sprite.groupcollide(ufos, bullets, True, True):
        ufo = Enemy('ufo.png', randint(50,650), 0, randint(1,3), 40, 40)
        ufos.add(ufo)
        ufo.rect.y = 0
        ufo.rect.x = randint(50, 650)
        n += 1
        Score = font.render('Убито: '+ str(n), True, (255,250,255))
        window.blit(Score, (50,50))
        if n >= 10:
            finish = True
            game = False
    display.update()
    clock.tick(FPS)

#if sprite.collide_rect():
# window.blit(win, (200,200)) 
#finish = True
#money.play()
#if sprite.collide_rect(player1, player2) or sprite.collide_rect(player1, w1) or sprite.collide_rect(player1, w2) or sprite.collide_rect(player1, w3) or sprite.collide_rect(player1, w4) or sprite.collide_rect(player1, w5):
#kick.play()
#player1.rect.x = 50
#player1.rect.y = 50