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

sstance_exp_images = os.listdir(path + '/SubzeroAnimations/Stance')
swalk_exp_images = os.listdir(path + '/SubzeroAnimations/Walking_Forward')
smhit_exp_images = os.listdir(path + '/SubzeroAnimations/PunchForward')
scstance_exp_images = os.listdir(path + '/ScorpionAnimations/ScStance')
scwalk_exp_images = os.listdir(path + '/ScorpionAnimations/ScWalkingForward')
scmhit_exp_images = os.listdir(path + '/ScorpionAnimations/ScPunchForward')

swalk_image_list = []

sstance_image_list = []

smhit_image_list = []

scwalk_image_list = []

scstance_image_list = []

scmhit_image_list = []

for img in sstance_exp_images:
    sstance_image_list.append(transform.scale(image.load('SubzeroAnimations/Stance/' + img), (playerstancewidth, playerstanceheight)))


for img in swalk_exp_images:
    swalk_image_list.append(transform.scale(image.load('SubzeroAnimations/Walking_Forward/' + img), (playerwalkingwidth, playerwalkingheight)))


for img in smhit_exp_images:
    smhit_image_list.append(transform.scale(image.load('SubzeroAnimations/PunchForward/' + img), (playerhitwidth, playerhitheight)))

for img1 in scstance_exp_images:
    new_img1 = transform.scale(image.load('ScorpionAnimations/ScStance/' + img1), (playerstancewidth, playerstanceheight))
    mirrored_img1 = transform.flip(new_img1, True, False)
    scstance_image_list.append(mirrored_img1)


for img2 in scwalk_exp_images:
    new_img2 = transform.scale(image.load('ScorpionAnimations/ScWalkingForward/' + img2), (playerwalkingwidth, playerwalkingheight))
    mirrored_img2 = transform.flip(new_img2, True, False)
    scstance_image_list.append(mirrored_img2)
                             


for img3 in scmhit_exp_images:
    new_img3 = transform.scale(image.load('ScorpionAnimations/ScPunchForward/' + img3), (playerhitwidth, playerhitheight))
    mirrored_img3 = transform.flip(new_img3, True, False)
    scstance_image_list.append(mirrored_img3)



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

class Player1(GameSprite):
    def __init__(self, sprite_img, width, height, x, y, speed, hp, stance_images, walking_images, hit_images, stance_list, walk_list, hit_list):
        super().__init__(sprite_img, width, height, x, y, speed, hp)
        #self.controls1 = controls1
        #self.controls2 = controls2
        self.stance_images = stance_images
        self.walking_images = walking_images
        self.hit_images = hit_images
        self.stance_list = stance_list
        self.walk_list = walk_list
        self.hit_list = hit_list
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
        else:
            self.swalking = 0
            self.sstil = 1

        
        if self.sdhit == 1:
            self.hit_animations()
        elif self.swalking == 1:
            self.walking_animations()
        else:
            self.stand_animations()
    def stand_animations(self):
        self.frames += 1
        if self.frames == 5:
                self.k += 1
                self.frames = 0
                if self.k == len(self.stance_list):
                    self.k = 0
                self.image = self.stance_images[self.k]
    def walking_animations(self):
        self.frames2 += 1
        if self.frames2 == 5:
                self.k2 += 1
                self.frames2 = 0
                if self.k2 == len(self.walk_list):
                    self.k2 = 0
                self.image = self.walking_images[self.k2]
    def hit_animations(self):
        self.timer = tm.time()
        self.frames3 += 1
        if self.frames3 == 5:
            self.k3 += 1
            self.frames3 = 0
            if self.k3 == len(self.hit_list):
                self.k3 = 0
                self.sdhit = 0
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

player1 = Player1(hero_image_test, width = playerhitwidth, height = playerhitheight, x = 200, y = HEIGHT-225, speed= 3, hp = 100, sstance_image_list, swalk_image_list, smhit_image_list, sstance_image_list, swalk_image_list, smhit_image_list)
player2 = Player1(hero_image_test, width = playerhitwidth, height = playerhitheight, x = 500, y = HEIGHT-225, speed= 3, hp = 100, scstance_image_list, scwalk_image_list, scmhit_image_list, scstance_image_list, scwalk_image_list, scmhit_image_list)

# основні змінні для гри

run = True
finish = False
clock = time.Clock()
FPS = 60
score = 0
lost = 0

last_hit_time = time.get_ticks()
hit_interval = 1000

# ігровий цикл

while run:
    # перевірка подій
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_KP1 and player1.sdhit != 1:
                now_time = time.get_ticks()
                if now_time - last_hit_time > hit_interval:
                    player1.sdhit = 1
                    player1.sstill = 1
                    player1.swalking = 1
    if not finish: # поки гра триває
        window.blit(bg_imaget, (0, 0))
        # рух спрайтів
        if tm.time() - player1.timer > 1:
            player1.timer = 0


        player1.draw()
        player1.update() #рух1 гравця
        player2.draw()
        player2.update() #рух2 гравця
    else:
        result_text.draw() # текст вкінці гри


    # оновлення екрану і FPS

    display.update()
    clock.tick(FPS)

    #transform.flip(image, True, False)