from pygame import *
from random import randint
import time as tm
import os

init()

font.init()

mixer.init()

punch_sound = mixer.Sound("Sounds/Punch.mp3")
ui_sound = mixer.Sound("Sounds/UiSound.mp3")
punchgethit_sound = mixer.Sound("Sounds/PunchGetHit.mp3")
kickgethit_sound = mixer.Sound("Sounds/KickGetHit.mp3")
parried_sound = mixer.Sound("Sounds/PunchParried.mp3")
fightstart_sound = mixer.Sound("Sounds/FightStartSound.mp3")
finishhim_sound = mixer.Sound("Sounds/FinishHimSound.mp3")

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
playergethitwidth, playergethitheight = 90, 153
scplayerstancewidth, scplayerstanceheight = 85, 150
scplayerwalkingwidth, scplayerwalkingheight = 100, 153
scplayerkickwidth, scplayerkickheight = 150, 150


# картинка фону
bg_image = image.load(test_image)

bg_imaget = transform.scale(bg_image, (900, 600))

#картинки для спрайтів

hero_image_test = image.load("ufo.png")

full_hpbar = image.load("Props\FullLifeBar.png")
empty_hpbar = image.load("Props\EmptyLifeBar.png")
ScorpionTextprop = image.load("Props\ScorpionText.png")
SubZeroTextprop = image.load("Props\SubZeroText.png")
FightTextProp = image.load("Props\FightProp.png")
Menu_startprop = image.load("Props\Menu_Start_screen.png")

path = os.getcwd()

sstance_exp_images = os.listdir(path + '/SubzeroAnimations/Stance')
swalk_exp_images = os.listdir(path + '/SubzeroAnimations/Walking_Forward')
smhit_exp_images = os.listdir(path + '/SubzeroAnimations/PunchForward')
skick_exp_images = os.listdir(path + '/SubzeroAnimations/Kick')
sgethit_exp_images = os.listdir(path + '/SubzeroAnimations/GettingHit')
sblocking_exp_images = os.listdir(path + '/SubzeroAnimations/Blocking')
scstance_exp_images = os.listdir(path + '/ScorpionAnimations/ScStance')
scwalk_exp_images = os.listdir(path + '/ScorpionAnimations/ScWalkingForward')
scmhit_exp_images = os.listdir(path + '/ScorpionAnimations/ScPunchForward')
sckick_exp_images = os.listdir(path + '/ScorpionAnimations/ScKick')
scgethit_exp_images = os.listdir(path + '/ScorpionAnimations/ScGetHit')
scblocking_exp_images = os.listdir(path + '/ScorpionAnimations/ScBlocking')

swalk_image_list = []

sstance_image_list = []

smhit_image_list = []

skick_image_list = []

sgethit_image_list = []

sblocking_image_list = []

scwalk_image_list = []

scstance_image_list = []

scmhit_image_list = []

sckick_image_list = []

scgethit_image_list = []

scblocking_image_list = []

for img in sstance_exp_images:
    sstance_image_list.append(transform.scale(image.load('SubzeroAnimations/Stance/' + img), (playerstancewidth, playerstanceheight)))


for img in swalk_exp_images:
    swalk_image_list.append(transform.scale(image.load('SubzeroAnimations/Walking_Forward/' + img), (playerwalkingwidth, playerwalkingheight)))


for img in smhit_exp_images:
    smhit_image_list.append(transform.scale(image.load('SubzeroAnimations/PunchForward/' + img), (playerhitwidth, playerhitheight)))

for img in skick_exp_images:
    skick_image_list.append(transform.scale(image.load('SubzeroAnimations/Kick/' + img), (playerhitwidth, playerhitheight)))

for img in sgethit_exp_images:
    sgethit_image_list.append(transform.scale(image.load('SubzeroAnimations/GettingHit/' + img), (playergethitwidth, playergethitheight)))

for img in sblocking_exp_images:
    sblocking_image_list.append(transform.scale(image.load('SubzeroAnimations/Blocking/' + img), (playerstancewidth, playerstanceheight)))

for img in scstance_exp_images:
    new_img1 = transform.scale(image.load('ScorpionAnimations/ScStance/' + img), (scplayerstancewidth, scplayerstanceheight))
    mirrored_img1 = transform.flip(new_img1, True, False)
    scstance_image_list.append(mirrored_img1)


for img in scwalk_exp_images:
    new_img2 = transform.scale(image.load('ScorpionAnimations/ScWalkingForward/' + img), (scplayerwalkingwidth, scplayerwalkingheight))
    mirrored_img2 = transform.flip(new_img2, True, False)
    scwalk_image_list.append(mirrored_img2)
                             


for img in scmhit_exp_images:
    new_img3 = transform.scale(image.load('ScorpionAnimations/ScPunchForward/' + img), (playerhitwidth, playerhitheight))
    mirrored_img3 = transform.flip(new_img3, True, False)
    scmhit_image_list.append(mirrored_img3)

for img in sckick_exp_images:
    new_img4 = transform.scale(image.load('ScorpionAnimations/ScKick/' + img), (scplayerkickwidth, scplayerkickheight))
    mirrored_img4 = transform.flip(new_img4, True, False)
    sckick_image_list.append(mirrored_img4)

for img in scgethit_exp_images:
    new_img5 = transform.scale(image.load('ScorpionAnimations/ScGetHit/' + img), (playergethitwidth, playergethitheight))
    mirrored_img5 = transform.flip(new_img5, True, False)
    scgethit_image_list.append(mirrored_img5)
for img in scblocking_exp_images:
    new_img6 = transform.scale(image.load('ScorpionAnimations/ScBlocking/' + img), (playerstancewidth, playerstanceheight))
    mirrored_img6 = transform.flip(new_img6, True, False)
    scblocking_image_list.append(mirrored_img6)



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
    def __init__(self, x, y, stance_images, walking_images, hit_images, kick_images, gethit_images, blocking_images, left_key, right_key, hit_key, kick_key, blocking_key): 
        super().__init__(stance_images[0], playerhitwidth, playerhitheight, x, y, 3, 100)

        self.stance_images = stance_images # списки картинок передаємо як змінні 
        self.walking_images = walking_images # і лише ці змінні використовуємо в класі
        self.hit_images = hit_images
        self.kick_images = kick_images
        self.gethit_images = gethit_images
        self.blocking_images = blocking_images

        self.left_key = left_key # назви кнопок для керування також передаємо як змінні
        self.right_key = right_key # і лише ці змінні використовуємо в класі, а не назви кнопок
        self.hit_key = hit_key
        self.kick_key = kick_key
        self.blocking_key = blocking_key
        self.is_hit = False

        self.timer = 0  
        self.k = 0 # достатньо 1 змінної k та frames ти ж одночасно лише 1 анімаціб показуєш
        self.frames = 0
        self.sstill = 1
        self.swalking = 0
        self.sdhit = 0
        self.skick = 0
        self.sgethit = 0
        self.sblocking = 0


    def update(self): #рух спрайту
        keys_pressed = key.get_pressed()
        if keys_pressed[self.left_key] and self.rect.x > 0 and sstartfight == True: # замість self.left_key підставлятимуться різні назви кнопок
            self.rect.x -= self.speed
            self.sstill = 0
            self.sblocking = 0
            self.swalking = 1
            self.sdhit = 0
        elif keys_pressed[self.right_key] and self.rect.x < player2.rect.centerx and self.rect.x < WIDTH - 70 and sstartfight == True:
            self.rect.x += self.speed
            self.sstill = 0
            self.sblocking = 0
            self.swalking = 1
            self.sdhit = 0
        else:
            self.swalking = 0
            self.sstil = 1

        
        if self.sdhit == 1:
            self.hit_animations()
        elif self.skick == 1:
            self.kick_animations()
        elif self.swalking == 1:
            if self.sgethit == 1:
                self.gethit_animations()
            else:
                self.walking_animations()
        elif self.sgethit == 1:
            self.gethit_animations()
        elif self.sblocking == 1:
            self.blocking_animations()
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
        self.frames += 1 
        if self.frames == 5:
            self.k += 1
            self.frames = 0
            if self.k >= len(self.hit_images):
                self.k = 0
                self.sdhit = 0
            self.image = self.hit_images[self.k]
    def kick_animations(self):
        self.frames += 1 
        if self.frames == 5:
            self.k += 1
            self.frames = 0
            if self.k >= len(self.kick_images):
                self.k = 0
                self.skick = 0
            self.image = self.kick_images[self.k]
    def gethit_animations(self):
        self.frames += 1 
        if self.frames == 5:
            self.k += 1
            self.frames = 0
            if self.k >= len(self.gethit_images):
                self.k = 0
                self.skick = 0
            self.image = self.gethit_images[self.k]
    def blocking_animations(self):
        self.frames += 1 # не треба змінних self.frames2 та self.k2 
        if self.frames == 5:
                self.k += 1
                self.frames = 0
                if self.k >= len(self.blocking_images):
                    self.k = 0
                self.image = self.blocking_images[self.k]

class Player2(Player1):
    def update(self): #рух спрайту
        keys_pressed = key.get_pressed()
        if keys_pressed[self.left_key] and self.rect.x > player1.rect.centerx and self.rect.x > 0 and sstartfight == True: # замість self.left_key підставлятимуться різні назви кнопок
            self.rect.x -= self.speed
            self.sstill = 0
            self.swalking = 1
            self.sblocking = 0
            self.sdhit = 0
        elif keys_pressed[self.right_key] and self.rect.x < WIDTH - 70 and sstartfight == True:
            self.rect.x += self.speed
            self.sstill = 0
            self.swalking = 1
            self.sblocking = 0
            self.sdhit = 0
        else:
            self.swalking = 0
            self.sstil = 1

        
        if self.sdhit == 1:
            self.sblocking = 0
            self.swalking = 0
            self.hit_animations()
        elif self.skick == 1:
            self.sblocking = 0
            self.kick_animations()
        elif self.swalking == 1:
            if self.sgethit == 1:
                self.sblocking = 0
                self.gethit_animations()
            else:
                self.sblocking = 0
                self.walking_animations()
        elif self.sgethit == 1:
            self.sblocking = 0
            self.gethit_animations()
        elif self.sblocking == 1:
            self.blocking_animations()
        else:
            self.stand_animations()



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
pl1hpwidth = 250
pl2hpwidth = 250
pl2x = 600

fullhpbarpl1 = GameSprite(full_hpbar, 250, 20, 50, 50, 0, 1)
emptyhpbarpl1 = GameSprite(empty_hpbar, 250, 20, 50, 50, 0, 1)
fullhpbarpl2 = GameSprite(full_hpbar, 250, 20, 500, 50, 0, 1)
emptyhpbarpl2 = GameSprite(empty_hpbar, 250, 20, 600, 50, 0, 1)
Subzeroctext = GameSprite(SubZeroTextprop, 75, 15, 50, 25, 0, 1)
Scorpctext = GameSprite(ScorpionTextprop, 75, 15, 750, 25, 0, 1)
fightctext = GameSprite(FightTextProp, 250, 125, -250, 250, 7, 1)
menuctext = GameSprite(Menu_startprop, 900, 600, 0, 0, 0, 1)


# напис з результатом гри

result_text = Text("Wins!", 250, 250, font_size = 50)

# створення спрайтів

player1 = Player1(100, HEIGHT-225, sstance_image_list, swalk_image_list, smhit_image_list, skick_image_list, sgethit_image_list, sblocking_image_list, K_a, K_d, K_q, K_e, K_f)
player2 = Player2(750, HEIGHT-225, scstance_image_list, scwalk_image_list, scmhit_image_list, sckick_image_list, scgethit_image_list, scblocking_image_list, K_LEFT, K_RIGHT, K_KP1, K_KP2, K_KP0)

# основні змінні для гри

run = True
finish = None
clock = time.Clock()
FPS = 60
score = 0
lost = 0
sstartfight = False
fightstartanim = False
endoffighttext = False
finhim = True
abletoblock1 = True
abletoblock2 = True

punchdmg = 5
kickdmg = 7

last_block_time1 = time.get_ticks()
last_block_time2 = time.get_ticks()
last_hit_time = time.get_ticks()
prefight_timec = time.get_ticks()
pre_fight_interval = 5000
hit_interval = 1500
block_interval = 750


# ігровий цикл

while run:
    # перевірка подій
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == player1.hit_key and player1.sdhit != 1:
                    if player1.swalking == 1:
                        pass
                    else:
                        punch_sound.play()
                    player1.sdhit = 1
                    player1.sblocking = 0
                    player1.k = 0
            if e.key == player2.hit_key and player2.sdhit != 1:
                    if player2.swalking == 1:
                        pass
                    else:
                        punch_sound.play()
                    player2.sdhit = 1
                    player2.sblocking = 0
                    player2.k = 0
            if e.key == player1.kick_key and player1.skick != 1:
                    if player1.swalking == 1:
                        pass
                    else:
                        punch_sound.play()
                    player1.skick = 1
                    player1.sblocking = 0
                    player1.k = 0
            if e.key == player2.kick_key and player2.skick != 1:
                    if player2.swalking == 1:
                        pass
                    else:
                        punch_sound.play()
                    player2.skick = 1
                    player2.sblocking = 0
                    player2.k = 0
            if e.key == player1.blocking_key and player1.sblocking != 1 and abletoblock1 == True:
                    player1.sblocking = 1
                    last_block_time1 = time.get_ticks()
                    abletoblock1 = False
            if e.key == player2.blocking_key and player1.sblocking != 1 and abletoblock2 == True:
                    player2.sblocking = 1
                    last_block_time2 = time.get_ticks()
                    abletoblock2 = False
            if not sstartfight:
                if e.key == K_SPACE:
                    prefight_timec = time.get_ticks()
                    sstartfight = True
                    finish = False
                    ui_sound.play()
                    fightstartanim = True
    if finish == None:
        menuctext.draw()
    if fightstartanim == True:
        window.blit(bg_imaget, (0, 0))
        player1.draw()
        player2.draw() 
        player1.update()
        player2.update()
        player1.speed = 0
        player2.speed = 0
        startanimtimer = time.get_ticks()
        if startanimtimer - prefight_timec > pre_fight_interval:
            fightstart_sound.play()
            fightstartanim = False

    if sstartfight == True and fightstartanim == False:
        player1.speed = 3
        player2.speed = 3
        if not finish: # поки гра триває
            window.blit(bg_imaget, (0, 0))
            # рух спрайтів
            current_time = time.get_ticks()
            if current_time - last_hit_time > hit_interval:
                player1.is_hit = False
                player2.is_hit = False
                player1.sgethit = 0
                player2.sgethit = 0
                last_hit_time = current_time
            if current_time - last_block_time1 > block_interval:
                abletoblock1 = True
            if current_time - last_block_time2 > block_interval:
                abletoblock2 = True
            if player1.sgethit == 1 and player1.sblocking == 0:
                player1.swalking = 0
                player1.sstil = 0
                player1.sdhit = 0
                player1.skick = 0
                if player1.rect.x > 0:
                    player1.rect.x -= player1.speed - 1
                else:
                    player1.sgethit = 0
                
            if player2.sgethit == 1:
                player2.swalking = 0
                player2.sstil = 0
                player2.sdhit = 0
                player2.skick = 0
                if player2.rect.x < WIDTH - 70 and player2.sblocking == 0:
                    player2.rect.x += player2.speed - 1
                else:
                    player2.sgethit = 0

            

            fullhpbarpl1 = GameSprite(full_hpbar, pl1hpwidth, 20, 50, 50, 0, 1)
            fullhpbarpl2 = GameSprite(full_hpbar, pl2hpwidth, 20, pl2x, 50, 0, 1)
            player1.draw()
            player2.draw()
            player1.update() #рух1 гравця
            player2.update() #рух2 гравця
            emptyhpbarpl1.draw()
            emptyhpbarpl2.draw()
            fullhpbarpl1.draw()
            fullhpbarpl2.draw()
            Scorpctext.draw()
            Subzeroctext.draw()
            if fightctext.rect.x == 1000:
                endoffighttext = True
            if endoffighttext == True:
                pass
            else:
                fightctext.draw()
                fightctext.rect.x += fightctext.speed
            if player1.rect.x > player2.rect.x - 50:
                player1.rect.x -= 3
            if player2.rect.x < player1.rect.x + 50:
                player2.rect.x += 3
            if sprite.collide_mask(player1, player2) and player1.sdhit == 1 and not player1.is_hit:
                last_hit_time = current_time
                player1.is_hit = True
                if player2.sblocking == 1:
                    parried_sound.play()
                    player2.hp -=  punchdmg - 4
                    player2.sblocking = 0
                    pl2hpwidth -= 2
                    pl2x += 2
                else:
                    punchgethit_sound.play()
                    player2.hp -=  punchdmg
                    pl2hpwidth -= 13
                    pl2x += 13
                    player2.sgethit = 1
            if sprite.collide_mask(player2, player1) and player2.sdhit == 1 and not player2.is_hit:
                last_hit_time = current_time
                player2.is_hit = True
                if player1.sblocking == 1:
                    parried_sound.play()
                    player1.hp -=  punchdmg - 4
                    player1.sblocking = 0
                    pl1hpwidth -= 2
                else:
                    punchgethit_sound.play()
                    player1.hp -=  punchdmg
                    pl1hpwidth -= 13
                    player1.sgethit = 1
            if sprite.collide_mask(player1, player2) and player1.skick == 1 and not player1.is_hit:
                last_hit_time = current_time
                player1.is_hit = True
                if player2.sblocking == 1:
                    parried_sound.play()
                    player2.hp -=  kickdmg - 6
                    player2.sblocking = 0
                    pl2hpwidth -= 2
                    pl2x += 2
                else:
                    kickgethit_sound.play()
                    player2.hp -=  kickdmg
                    pl2hpwidth -= 13
                    pl2x += 13
                    player2.sgethit = 1
            if sprite.collide_mask(player2, player1) and player2.skick == 1 and not player2.is_hit:
                last_hit_time = current_time
                player2.is_hit = True
                if player1.sblocking == 1:
                    parried_sound.play()
                    player1.hp -=  kickdmg - 6
                    player1.sblocking = 0
                    pl1hpwidth -= 2
                else:
                    kickgethit_sound.play()
                    player1.hp -=  kickdmg
                    pl1hpwidth -= 13
                    player1.sgethit = 1
            if player1.hp <= 5 and finhim == True:
                finishhim_sound.play()
                finhim = False
            elif player2.hp <= 5 and finhim == True:
                finishhim_sound.play()
                finhim = False
            if player1.hp <= 0:
                result_text.set_text("Player 2, Wins!")
                finish = True
            elif player2.hp <= 0:
                result_text.set_text("Player 1, Wins!")
                finish = True
        else:
            result_text.draw() # текст вкінці гри


    # оновлення екрану і FPS

    display.update()
    clock.tick(FPS)

    #transform.flip(image, True, False)