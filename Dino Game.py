import pygame, sys, random
from pygame.locals import *
import time
import random
pygame.init()
mainClock = pygame.time.Clock()
W_W = 1370
W_H = 715
W_W_P = 70
W_H_P = 280
W_W_K1 = 1370
W_H_K1 = 320
W_W_K2 = 1370
W_H_K2 = 350
w = pygame.display.set_mode((W_W, W_H), 0, 32)
pygame.display.set_caption('Dino Game')
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LGREEN =(127,255,0)
WHITE = (255, 255, 255)
RED =(220,20,60)
PINK = (255,200,250)
#moteghaier haie asly bazi.
MOVESPEED = 80
f = ['kak1.png','kak2.png']
kaks = []
d = random.choice(f)
if d == 'kak2.png':
    a = 800
    b = 350
else:
    a = 500
    b = 320
player = pygame.Rect(W_W_P, W_H_P, 158, 172)
playeri = pygame.image.load('Dino.png')
playerSi = pygame.transform.scale(playeri, (130, 134))
mus = pygame.mixer.music.load('DODFO.mp3')
pygame.mixer.music.play(-1, 0.0)
kak1 = pygame.Rect(a, b, 192, 380)
kak1i = pygame.image.load(d)
kak1Si = pygame.transform.scale(kak1i, (52, 130))
zam = pygame.Rect(685, 450, 2404, 28)
zami = pygame.image.load('Track.png')
son = pygame.mixer.Sound('df.wav')
kakCounter = 0
NEWKAK = 5
w.blit(playerSi, player)
w.blit(kak1Si, kak1)
moveUp = False
while True:
    pygame.mixer.music.play(-1, 0.0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_SPACE:
                moveLeft = True
            if event.key == K_UP or event.key == K_SPACE:
                moveUp = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_UP or event.key == K_SPACE:
                moveUp = False
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
    kakCounter += 1
    if kakCounter >= NEWKAK:
        kakCounter = 5
        kaks.append(pygame.Rect(random.randint(0, W_W - 20), random.randint(0, W_H - 20), 20, 20))
    w.fill(WHITE)
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft or kak1.left < 0:
        kak1.left += 10
    w.blit(playerSi, player)
    w.blit(kak1Si, kak1)
    if W_W_K1 == 0:
        W_W_K1 += 715
    for k in kaks[:]:
        if player.colliderect(kak1):
            bacicfont = pygame.font.SysFont(None,70)
            text = bacicfont.render('GAME OVER',True,BLACK,WHITE)
            w.blit(text,(685,476))
        
            
        
    pygame.display.update()
    mainClock.tick(40)
