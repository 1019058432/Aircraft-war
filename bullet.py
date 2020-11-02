import pygame
import plane
import main
import sys
from main import *

class Bullet(object):

    def __init__(self, x, y, u, d, screen):
        # 子弹位置
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet-3.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.right = y - 90
        self.rect.top = u
        self.rect.bottom = d - 150
        self.remo2=plane.EnemyPlane
        # self.Pu=PublicEnemyPlane(screen)

    def display(self):
        self.screen.blit(self.image, self.rect)

    def move(self,l):
        self.rect.top -= 1

class EnBullet(object):
    def __init__(self, x, y, u, d, screen,hero):
        # 子弹位置
        self.screen = screen
        self.image = pygame.image.load("./feiji/bel.png").convert()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.right = y - 60
        self.rect.top = u
        self.rect.bottom = d  # -150
        #hero位置
        self.Hero=hero

    def display(self):
        # 更新敌机位置
        self.screen.blit(self.image, self.rect)

    # 敌机1子弹方向
    def move(self):
        self.rect.top += 2
        if (self.rect.left>self.Hero.rect.left+60) and(self.rect.left<self.Hero.rect.right-60):
            if (self.rect.top>self.Hero.rect.top)and(self.rect.top<self.Hero.rect.bottom):
                self.Hero.life=False
                self.Hero.reset()
                #sys.quit()

