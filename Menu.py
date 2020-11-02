import pygame
from pygame.locals import *
import main
import imp
import plane
pygame.init()
class SeletPlane(object):
    def __init__(self, screen):
        self.select_image = './feiji/uiPlane0.png'
        self.background_game = pygame.image.load(self.select_image).convert()
        # 获得以及设计飞机坐标
        self.rect = self.background_game.get_rect()
        self.screen=screen
        self.rect.left = 80
        self.rect.bottom = 725

        #信号
        self.Start=False
        self.Exit=False
    def display(self):
        #飞机位置
        self.screen.blit(self.background_game, self.rect)
    def Statu(self):
        if self.rect.top==488:
            if main.Runing==False:
                self.Start=True
                imp.reload(main)            #接入游戏
                main.start()

            else:
                main.start()
        elif self.rect.top==588:
            #血量为0或者负值时不可继续（未完成）
            if main.Blood<=0:
                imp.reload(main)  # 接入游戏
                main.Blood=5
                main.start()
            else:
                main.Runing = True
        elif self.rect.top==688:
            self.Exit=True

    def move_up(self):
        if self.rect.top>525:
            self.rect.top -= 100

    def move_down(self):
        if self.rect.bottom < 725:
            self.rect.top += 100



def desk():
    screen = pygame.display.set_mode((480, 800), 0, 32)
    background_image = './feiji/background.png'
    background_game = pygame.image.load(background_image).convert()
    my_font = pygame.font.Font('./font/simsun.ttc', 50)
    text='飞机大战'
    font_image = my_font.render(text, True, (0, 255,0))
    select_image1=select(20,'Star Game',(255,255,255))
    select_image2 = select(20,'Continue Game',(255,255,255))
    select_image3 = select(20,'Exit',(255,255,255))
    select_game = SeletPlane(screen)
    Running=True
    while Running:
        screen.blit(background_game, (0, 0))
        screen.blit(font_image, (125, 50))
        screen.blit(select_image1, (125, 500))
        screen.blit(select_image2, (125, 600))
        screen.blit(select_image3, (125, 700))
        select_game.display()
        # 事件监控
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key ==K_a or event.key==K_LEFT:
                    print()
                elif event.key ==K_d or event.key==K_RIGHT:
                    print()
                elif event.key ==K_w or event.key==K_UP:
                    select_game.move_up()
                elif event.key ==K_s or event.key==K_DOWN:
                    select_game.move_down()
                elif event.key==K_SPACE:
                    select_game.Statu()
                    Running=False

        pygame.display.update()
def  select(Size,Text,color):
    select_font = pygame.font.Font('./font/simsun.ttc',Size)
    text = Text
    select_image = select_font.render(text, True, color)
    return select_image

if __name__ == '__main__':
        desk()
