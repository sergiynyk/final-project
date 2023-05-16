from pygame import *
from random import randint
import time as tm
import os

init()

font.init()

mixer.init()

# розміри вікна
test_image = None

map_get = randint(3, 4)
if map_get == 2:
    test_image = "Maps/map2.png"
elif map_get == 3:
    test_image = "Maps/map3.png"
elif map_get == 4:
    test_image = "Maps/map4.png"


WIDTH, HEIGHT = 900, 600

playerstancewidth, playerstanceheight = 75, 150
playerwalkingwidth, playerwalkingheight = 100, 153
playerhitwidth, playerhitheight = 140, 150

# картинка фону
bg_image = image.load(test_image)

bg_imaget = transform.scale(bg_image, (900, 600))

#картинки для спрайтів

hero_image_test = image.load("ufo.png")

path = os.getcwd()

stance_exp_images = os.listdir(path + '/SubzeroAnimations/Stance')
walk_exp_images = os.listdir(path + '/SubzeroAnimations/Walking_Forward')
hit_exp_images = os.listdir(path + '/SubzeroAnimations/PunchForward')

walk_image_list = []

stance_image_list = []

hit_image_list = []

for img in stance_exp_images:
    stance_image_list.append(transform.scale(image.load('SubzeroAnimations/Stance/' + img), (playerstancewidth, playerstanceheight)))


for img in walk_exp_images:
    walk_image_list.append(transform.scale(image.load('SubzeroAnimations/Walking_Forward/' + img), (playerwalkingwidth, playerwalkingheight)))


for img in hit_exp_images:
    hit_image_list.append(transform.scale(image.load('SubzeroAnimations/PunchForward/' + img), (playerhitwidth, playerhitheight)))



# класи

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y, speed, hp):
        super().__init__()
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.mask = mask.from_surface(self.image)
        self.hp = hp


    def draw(self): #відрисовуємо спрайт у вікні
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, sprite_img, width, height, x, y, speed, hp):
        super().__init__(sprite_img, width, height, x, y, speed, hp)
        self.stance_images = stance_image_list
        self.walking_images = walk_image_list
        self.hit_images = hit_image_list
        self.timer = 0
        self.k = 0
        self.k2 = 0
        self.k3 = 0
        self.frames = 0
        self.frames2 = 0
        self.frames3 = 0
        self.sstill = 1
        self.swalking = 0
        self.sdhit = 0
    def update(self): #рух спрайту
        keys_pressed = key.get_pressed()
        if not keys_pressed[K_LEFT] and not keys_pressed[K_RIGHT]:
            self.sstill = 1
            self.swalking = 0
            self.sdhit = 0
        if keys_pressed[K_e] and not keys_pressed[K_LEFT] and not keys_pressed[K_RIGHT]:
            self.sstill = 0
            self.swalking = 0
            self.sdhit = 1
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.sstill = 0
            self.swalking = 1
            self.sdhit = 0
        if keys_pressed[K_RIGHT] and self.rect.x < WIDTH - 70:
            self.rect.x += self.speed
            self.sstill = 0
            self.swalking = 1
            self.sdhit = 0
        if self.sstill == 1:
            self.stand_animations()
        if self.swalking == 1:
            self.walking_animations()
        if self.sdhit == 1:
            self.hit_animations()
    def stand_animations(self):
        self.frames += 1
        if self.frames == 5:
                self.k += 1
                self.frames = 0
                if self.k == len(stance_image_list):
                    self.k = 0
                self.image = self.stance_images[self.k]
    def walking_animations(self):
        self.frames2 += 1
        if self.frames2 == 5:
                self.k2 += 1
                self.frames2 = 0
                if self.k2 == len(walk_image_list):
                    self.k2 = 0
                self.image = self.walking_images[self.k2]
    def hit_animations(self):
        self.timer = tm.time()
        self.frames3 += 1
        if self.frames3 == 5 and self.timer >= 3:
            self.k3 += 1
            self.frames3 = 0
            if self.k3 == len(hit_image_list):
                self.k3 = 0
                self.timer = tm.time()
            self.image = self.hit_images[self.k3]


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

# створення спрайтів

player = Player(hero_image_test, width = playerhitwidth, height = playerhitheight, x = 200, y = HEIGHT-225, speed= 3, hp = 100)


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
        if player.k3 == len(hit_image_list):
            player.timer = tm.time()
        player.draw()
        player.update() #рух гравця
    else:
        result_text.draw() # текст вкінці гри


    # оновлення екрану і FPS

    display.update()
    clock.tick(FPS)

    #transform.flip(image, True, False)