import pygame
import time
import random
from pygame import mixer

pygame.init()

BLACK=(0,0,0)
BROWN=(128, 64, 64)

wn_width = 400
wn_height = 500
wn = pygame.display.set_mode((wn_width, wn_height))
pygame.display.set_caption("flappy Bird")

#images
bgIm=pygame.image.load("images/bird_bg.png")
birdIm = pygame.image.load("images/bird.png")

#bottom_b = the bottom edge of the screen
bottom_b = 446

#obstacles
class obstacles():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gap = 180
        self.speedx = -0.5
        self.passed = 0

    def update(self):
        self.x = self.x + self.speedx

    #checking for collisions

        if self.x + self.width<0:
            self.x = wn_width
            self.width = random.randint(30,150)
            self.height = random.randint(40, 280)
            self.passed = self.passed + 1

    def draw(self, wn):

        pygame.draw.rect(wn, BROWN, (self.x, 0, self.width, self.height))
        bottom_blk_y=self.height+self.gap
        bottom_blk_height = bottom_b - bottom_blk_y
        pygame.draw.rect(wn, BROWN, (self.x, bottom_blk_y, self.width, bottom_blk_height))


class Player():
    def __init__(self):
        self.image=birdIm
        self.width = self.image.get_width()
        self.height=self.image.get_height()
        self.x=int(wn_width/6)
        self.y=int(wn_height/2-60)
        self.speedy=1

    def update(self):
        keystate=pygame.key.get_pressed()
        if (keystate[pygame.K_SPACE]) & (self.speedy >= 1) :

            while self.speedy >= -2.2:
                self.speedy = self.speedy - 0.275


        elif self.speedy < 1:
            self.speedy= self.speedy +0.0275

        self.y = self.y + self.speedy
        if self.y + self.height>bottom_b:
            self.y = bottom_b - self.height
        if self.y <= 0:
            self.y =  0


def score_board(passed):
    font=pygame.font.Font(None, 20)
    text = font.render(f"Passed: {passed}", True, BLACK)
    wn.blit(text, (0, 10))
    pygame.display.update()

def crash():
    font=pygame.font.Font(None, 70)
    text2 = font.render(f"score: {passed}", True, BLACK)
    text = font.render("You Crashed!", True, BLACK)

    text_width = text.get_width()
    text_height = text.get_height()
    x=int(wn_width/2-text_width/2)
    y=150
    wn.blit(text2, (x + 20,y + 75))
    wn.blit(text, (x,y))
    pygame.display.update()
    time.sleep(3)
    game_loop()

def play_sound():
    mixer.music.load('audio/flappybirdgamemusic.mp3')
    mixer.music.play(-1)

def game_loop():
    global passed
    block_width= random.randint(30, 150)
    block_height = random.randint(40, 280)
    block_x = wn_width
    block_y = 0



    block = obstacles(block_x, block_y, block_width, block_height)
    player=Player()

    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        player.update()
        block.update()

        passed = block.passed

        score_board(block.passed)
        wn.blit(bgIm, (0,0))
        wn.blit(player.image, (player.x, player.y))
        block.draw(wn)

        #check for collisions
        bottom_blk_height=block.height+block.gap
        if player.x + player.width>block.x and player.x < block.x + block.width:
            if player.y<block.height or player.y + player.height > bottom_blk_height:
                crash()





        pygame.display.update()

play_sound()
game_loop()

#quit game
pygame.quit()
quit()