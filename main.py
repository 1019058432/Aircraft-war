import pygame
import time
from pygame.locals import *
from plane import *
from bullet import *
from public import *
import HeroLife
import Menu
pygame.init()
Runing = True
Blood=0
def start():#开始游戏
    #背景
    global Runing
    screen =pygame.display.set_mode((480,800))
    background_image='./feiji/background.png'
    background_game=pygame.image.load(background_image).convert()
    # 音乐
    pygame.mixer.init()
    BGM = './font/music.mp3'
    pygame.mixer.music.load(BGM)
    #飞机
    hero_plane=HeroPlane(screen)
    Life=HeroLife.lifePlane(screen)
    enemy_plane = EnemyPlane(screen)
    bul = bullet.Bullet
    enemy_plane2 = EnemyPlane2(screen)
    enemy_plane3 = EnemyPlane3(screen)
    #血
    Blood=hero_plane.Blood
    #击毁飞机数
    hero_couse = pygame.font.Font(None, 50)
    #刷新速率
    Clock=pygame.time.Clock()
    if Runing:
        pygame.mixer.music.play(-1)
    if Runing==False:
        pygame.mixer.music.stop()
    while Runing:
        screen.blit(background_game,(0,0))
        en1 = enemy_plane#敌机1位置
        en2 = enemy_plane2  # 敌机1位置
        en3 = enemy_plane3  # 敌机1位置
        hero_plane.display(en1)
        Life.display()
        hero_plane.reMove(en1)
        hero_plane.reMove2(en2)
        hero_plane.reMove3(en3)
        #敌机加载；移动
        enemy_plane.display(hero_plane)
        enemy_plane2.display(hero_plane)
        enemy_plane3.display(hero_plane)
        enemy_plane3.move()
        enemy_plane2.move()
        enemy_plane.move()

        #生命耗尽
        if hero_plane.Blood==0:
            Runing=False
            Menu.desk()

        #事件监控
        for event in pygame.event.get():

            if event.type ==QUIT :
                print("Exit Game")
                Runing=False
                Menu.desk()
                #exit()

            elif event.type == KEYDOWN :
                if event.key ==K_a or event.key==K_LEFT:
                    hero_plane.move_left=True
                elif event.key ==K_d or event.key==K_RIGHT:
                    hero_plane.move_ringht=True
                elif event.key ==K_w or event.key==K_UP:
                    hero_plane.move_up=True
                elif event.key ==K_s or event.key==K_DOWN:
                    hero_plane.move_down=True
                elif event.key==K_SPACE:
                    hero_plane.bullets=True
            elif event.type == KEYUP :
                if event.key ==K_a or event.key==K_LEFT:
                    hero_plane.move_left=False
                elif event.key ==K_d or event.key==K_RIGHT:
                    hero_plane.move_ringht=False
                elif event.key ==K_w or event.key==K_UP:
                    hero_plane.move_up=False
                elif event.key ==K_s or event.key==K_DOWN:
                    hero_plane.move_down=False
                elif event.key==K_SPACE:
                    hero_plane.bullets=False

        hero_plane.move_plane()
        hero_plane.launch_bullet()
        enemy_plane.launch_bullet(hero_plane)
        enemy_plane2.launch_bullet(hero_plane)
        enemy_plane3.launch_bullet(hero_plane)
        #碰撞
        if (hero_plane.rect.midtop<en1.rect.midtop)and(hero_plane.rect.center>en1.rect.center):
            hero_plane.life=False
            hero_plane.reset()
            enemy_plane.reset()
        if (hero_plane.rect.midtop<en2.rect.midtop)and(hero_plane.rect.center>en2.rect.center):
            hero_plane.life=False
            hero_plane.reset()
            enemy_plane2.reset()
        if (hero_plane.rect.midtop<en3.rect.midtop)and(hero_plane.rect.center>en3.rect.center):
            hero_plane.life=False
            hero_plane.reset()
            enemy_plane3.reset()

        hit_number=str(enemy_plane.couse+enemy_plane2.couse+enemy_plane3.couse)#击毁飞机数量
        hero_couse_image = hero_couse.render(hit_number, True,(255, 255, 255))
        screen.blit(hero_couse_image, (10, 10))
        heroLife = str(hero_plane.Blood)  # 击毁飞机数量
        hero_Life_image = hero_couse.render(heroLife, True, (255, 255, 255))
        screen.blit(hero_Life_image, (410, 0))
        Clock.tick(120)
        #time.sleep(0.002)
        pygame.display.update()
def Exit():
    print('exit')

#def
if __name__=='__main__':
        start()