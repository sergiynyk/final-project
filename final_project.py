from pygame import *
from random import randint
import time as tm
import os

init()
font.init()
mixer.init()

# розміри вікна
WIDTH, HEIGHT = 900, 600
playerwidth, playerheight = 75, 150

# картинка фону
bg_image = image.load("background1.png")
bg_imaget = transform.scale(bg_image, (1200, 600))
#картинки для спрайтів
player_image = image.load("Animations/Stance/Stance1.png")
ufo_image = image.load("ufo.png")

path = os.getcwd()
stance_exp_images = os.listdir(path + '/Animations/Stance')
walk_exp_images = os.listdir(path + '/Animations/Walking_Forward')
walk_image_list = []
stance_image_list = []
for img in stance_exp_images:
    stance_image_list.append(transform.scale(image.load('Animations/Stance/' + img), (playerwidth, playerheight)))
for img in walk_exp_images:
    walk_image_list.append(transform.scale(image.load('Animations/Walking_Forward/' + img), (playerwidth, playerheight)))
#положення наразі:


# класи
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y, speed):
        super().__init__()
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.mask = mask.from_surface(self.image)

        self.images = stance_image_list
        self.k = 0
        self.k2 = 0
        self.frames = 0
        self.frames2 = 0
        self.sstill = 1
        self.swalking = 0

    def draw(self): #відрисовуємо спрайт у вікні
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self): #рух спрайту
        keys_pressed = key.get_pressed()
        if not keys_pressed[K_LEFT] and not keys_pressed[K_RIGHT]:
            self.sstill = 1
            self.swalking = 0
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.sstill = 0
            self.swalking = 1
        if keys_pressed[K_RIGHT] and self.rect.x < WIDTH - 70:
            self.rect.x += self.speed
            self.sstill = 0
            self.swalking = 1
        if self.sstill == 1:
            self.stand_animations()
        if self.swalking == 1:
            self.walking_animations()
    def stand_animations(self):
        self.frames += 1
        if self.frames == 5:
                self.k += 1
                self.frames = 0
                if self.k == len(stance_image_list):
                    self.k = 0
                self.image = self.images[self.k]
    def walking_animations(self):
        self.frames2 += 1
        if self.frames2 == 5:
                self.k2 += 1
                self.frames2 = 0
                if self.k2 == len(walk_image_list):
                    self.k2 = 0
                self.image = self.images[self.k2]
    


            
        


        
class Text(sprite.Sprite):
    def __init__(self, text, x, y, font_size=22, font_name="Impact", color=(255,255,255)):
        self.font = font.SysFont(font_name, font_size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        
    def draw(self): #відрисовуємо спрайт у вікні
        window.blit(self.image, self.rect)
    
    def set_text(self, new_text): #змінюємо текст напису
        self.image = self.font.render(new_text, True, self.color)


# створення вікна
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Шутер")

# написи для лічильників очок
score_text = Text("Рахунок: 0", 20, 50)
# напис з результатом гри
result_text = Text("Перемога!", 350, 250, font_size = 50)

#додавання фону

# створення спрайтів
player = Player(player_image, width = playerwidth, height = playerheight, x = 200, y = HEIGHT-150, speed= 3)


# основні змінні для гри
run = True
finish = False
clock = time.Clock()
FPS = 60
score = 0
lost = 0

# ігровий цикл
while run:
    # перевірка подій
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            pass
    if not finish: # поки гра триває
        window.blit(bg_imaget, (0, 0)) 
        # рух спрайтів
        player.draw()
        player.update() #рух гравця
    else:
        result_text.draw() # текст вкінці гри
    score_text.draw()
    # оновлення екрану і FPS
    display.update()
    clock.tick(FPS)