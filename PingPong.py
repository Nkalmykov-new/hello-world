from pygame import *

window = display.set_mode((800, 600))
display.set_caption('АэроХоккей')

background = transform.scale(image.load('AeroHockey.jpg'), (800, 600))

clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('GOAL.mp3')
#End = mixer.Sound('End_match.mp3')

Score_1 = 0
Score_2 = 0

font.init()
font = font.SysFont('Arial', 24)
pl1 = font.render('Игрок первый :'+ str(Score_1), True, (0,0,0))
pl2 = font.render('Игрок второй :'+ str(Score_2), True, (0,0,0))

win_1 = font.render('ИГРОК ПЕРВЫЙ ВЫИГРАЛ', True, (0,0,0))
win_2 = font.render('ИГРОК ВТОРОЙ ВЫИГРАЛ', True, (0,0,0))

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
        if keys_pressed[K_w] and Player1.rect.y > 10:
            Player1.rect.y -= self.speed
        if keys_pressed[K_s] and Player1.rect.y < 550:
            Player1.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and Player2.rect.y > 10:
            Player2.rect.y -= self.speed
        if keys_pressed[K_DOWN] and Player2.rect.y < 550:
            Player2.rect.y += self.speed

class Shaiba(GameSprite):
    def update(self):
        pass

Player1 = Player('Bita.png', 100, 280, 5, 70, 70)
Player2 = Player2('Bita2.png', 700, 280, 5, 70, 70)
Shaiba = Shaiba('Shaiba.png', 380, 280, 0, 40, 40)

ball_x = 5
ball_y = 5

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        Shaiba.rect.x += ball_x
        Shaiba.rect.y += ball_y
        window.blit(background,(0,0))

    if Shaiba.rect.y > 550 or Shaiba.rect.y < 0:
        ball_y *= -1
    
    window.blit(pl1, (50,50))
    window.blit(pl2, (590,50))

    Player1.reset()
    Player1.update()

    Player2.reset()
    Player2.update()

    Shaiba.reset()
    Shaiba.update()

    if sprite.collide_rect(Player1, Shaiba) or sprite.collide_rect(Player2, Shaiba):
        ball_x *= -1

    if Shaiba.rect.x < 0:
        Score_2 += 1
        pl2 = font.render('Игрок второй :'+ str(Score_2), True, (0,0,0))
        mixer.music.play()
        Shaiba.rect.x = 380
        Shaiba.rect.y = 280
        ball_x = -5
        ball_y = 5

    if Shaiba.rect.x > 800:
        Score_1 += 1
        pl1 = font.render('Игрок первый :'+ str(Score_1), True, (0,0,0))
        mixer.music.play()
        Shaiba.rect.x = 380
        Shaiba.rect.y = 280
        ball_x = 5
        ball_y = 5

    if Score_1 == 7:
        window.blit(win_1, (300,280))
        ball_x = 0
        ball_y = 0

    if Score_2 == 7:
        window.blit(win_2, (300,280))
        ball_x = 0
        ball_y = 0

    display.update()
    clock.tick(FPS)
