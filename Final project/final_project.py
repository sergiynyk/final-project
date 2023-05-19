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
skick_exp_images = os.listdir(path + '/SubzeroAnimations/Kick')
scstance_exp_images = os.listdir(path + '/ScorpionAnimations/ScStance')
scwalk_exp_images = os.listdir(path + '/ScorpionAnimations/ScWalkingForward')
scmhit_exp_images = os.listdir(path + '/ScorpionAnimations/ScPunchForward')
sckick_exp_images = os.listdir(path + '/ScorpionAnimations/ScKick')

swalk_image_list = []

sstance_image_list = []

smhit_image_list = []

skick_image_list = []

scwalk_image_list = []

scstance_image_list = []

scmhit_image_list = []

sckick_image_list = []

for img in sstance_exp_images:
    sstance_image_list.append(transform.scale(image.load('SubzeroAnimations/Stance/' + img), (playerstancewidth, playerstanceheight)))


for img in swalk_exp_images:
    swalk_image_list.append(transform.scale(image.load('SubzeroAnimations/Walking_Forward/' + img), (playerwalkingwidth, playerwalkingheight)))


for img in smhit_exp_images:
    smhit_image_list.append(transform.scale(image.load('SubzeroAnimations/PunchForward/' + img), (playerhitwidth, playerhitheight)))

for img in skick_exp_images:
    skick_image_list.append(transform.scale(image.load('SubzeroAnimations/Kick/' + img), (playerhitwidth, playerhitheight)))

for img in scstance_exp_images:
    new_img1 = transform.scale(image.load('ScorpionAnimations/ScStance/' + img), (playerstancewidth, playerstanceheight))
    mirrored_img1 = transform.flip(new_img1, True, False)
    scstance_image_list.append(mirrored_img1)


for img in scwalk_exp_images:
    new_img2 = transform.scale(image.load('ScorpionAnimations/ScWalkingForward/' + img), (playerwalkingwidth, playerwalkingheight))
    mirrored_img2 = transform.flip(new_img2, True, False)
    scwalk_image_list.append(mirrored_img2)
                             


for img in scmhit_exp_images:
    new_img3 = transform.scale(image.load('ScorpionAnimations/ScPunchForward/' + img), (playerhitwidth, playerhitheight))
    mirrored_img3 = transform.flip(new_img3, True, False)
    scmhit_image_list.append(mirrored_img3)

for img in sckick_exp_images:
    new_img4 = transform.scale(image.load('ScorpionAnimations/ScKick/' + img), (playerhitwidth, playerhitheight))
    mirrored_img4 = transform.flip(new_img4, True, False)
    sckick_image_list.append(mirrored_img4)



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
    # в дужках передаємо лише ті змінні які різні для різних гравців - списки картинок і назви кнопок
    def __init__(self, x, y, stance_images, walking_images, hit_images, kick_images, left_key, right_key, hit_key, kick_key): 
        super().__init__(stance_images[0], playerhitwidth, playerhitheight, x, y, 3, 100)

        self.stance_images = stance_images # списки картинок передаємо як змінні 
        self.walking_images = walking_images # і лише ці змінні використовуємо в класі
        self.hit_images = hit_images
        self.kick_images = kick_images

        self.left_key = left_key # назви кнопок для керування також передаємо як змінні
        self.right_key = right_key # і лише ці змінні використовуємо в класі, а не назви кнопок
        self.hit_key = hit_key
        self.kick_key = kick_key

        self.timer = 0  
        self.k = 0 # достатньо 1 змінної k та frames ти ж одночасно лише 1 анімаціб показуєш
        self.frames = 0
        self.sstill = 1
        self.swalking = 0
        self.sdhit = 0
        self.skick = 0


    def update(self): #рух спрайту
        keys_pressed = key.get_pressed()
        if keys_pressed[self.left_key] and self.rect.x > 0: # замість self.left_key підставлятимуться різні назви кнопок
            self.rect.x -= self.speed
            self.sstill = 0
            self.swalking = 1
            self.sdhit = 0
        elif keys_pressed[self.right_key] and self.rect.x < WIDTH - 70:
            self.rect.x += self.speed
            self.sstill = 0
            self.swalking = 1
            self.sdhit = 0
        else:
            self.swalking = 0
            self.sstil = 1

        
        if self.sdhit == 1:
            self.hit_animations()
        if self.skick == 1:
            self.kick_animations()
        elif self.swalking == 1:
            self.walking_animations()
        else:
            self.stand_animations()


    def stand_animations(self):
        self.frames += 1
        if self.frames == 5:
                self.k += 1
                self.frames = 0
                if self.k >= len(self.stance_images): # тут не потрібно окрмо список з назвами картинок
                    self.k = 0                          #можна  виконаристати self.stance_images
                self.image = self.stance_images[self.k]


    def walking_animations(self):
        self.frames += 1 # не треба змінних self.frames2 та self.k2 
        if self.frames == 5:
                self.k += 1
                self.frames = 0
                if self.k >= len(self.walking_images):
                    self.k = 0
                self.image = self.walking_images[self.k]
    def hit_animations(self):
        self.timer = tm.time()
        self.frames += 1 
        if self.frames == 5:
            self.k += 1
            self.frames = 0
            if self.k >= len(self.hit_images):
                self.k = 0
                self.sdhit = 0
            self.image = self.hit_images[self.k]
    def kick_animations(self):
        self.timer = tm.time()
        self.frames += 1 
        if self.frames == 5:
            self.k += 1
            self.frames = 0
            if self.k >= len(self.kick_images):
                self.k = 0
                self.skick = 0
            self.image = self.kick_images[self.k]



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

player1 = Player1(200, HEIGHT-225, sstance_image_list, swalk_image_list, smhit_image_list, skick_image_list, K_a, K_d, K_e, K_q)
player2 = Player1(500, HEIGHT-225, scstance_image_list, scwalk_image_list, scmhit_image_list, sckick_image_list, K_LEFT, K_RIGHT, K_KP1, K_KP2)

# основні змінні для гри

run = True
finish = False
clock = time.Clock()
FPS = 60
score = 0
lost = 0

last_hit_time1 = time.get_ticks()
last_hit_time2 = time.get_ticks()
last_hit_time3 = time.get_ticks()
last_hit_time4 = time.get_ticks()
hit_interval = 1000


# ігровий цикл

while run:
    # перевірка подій
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == player1.hit_key and player1.sdhit != 1:
                now_time = time.get_ticks()
                if now_time - last_hit_time1 > hit_interval:
                    player1.sdhit = 1
                    player1.sstill = 1
                    player1.swalking = 1
            if e.key == player2.hit_key and player2.sdhit != 1:
                now_time = time.get_ticks()
                if now_time - last_hit_time2 > hit_interval:
                    player2.sdhit = 1
                    player2.sstill = 1
                    player2.swalking = 1
            if e.key == player1.kick_key and player1.skick != 1:
                now_time = time.get_ticks()
                if now_time - last_hit_time3 > hit_interval:
                    player1.sdhit = 1
                    player1.sstill = 1
                    player1.swalking = 1
            if e.key == player2.kick_key and player2.skick != 1:
                now_time = time.get_ticks()
                if now_time - last_hit_time4 > hit_interval:
                    player2.skick = 1
                    player2.sstill = 1
                    player2.swalking = 1
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
