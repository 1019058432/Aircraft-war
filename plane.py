import random
import time

from public import*
import pygame
import bullet

class HeroPlane(object):
    def __init__(self,screen):
        #飞机图
        self.screen =screen
        self.image_name="./feiji/her.png"
        self.image =pygame.image.load(self.image_name).convert()
        #获得以及设计飞机坐标
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
        #
        self.life=True
        #持续移动信号
        self.move_up=False
        self.move_down=False
        self.move_left=False
        self.move_ringht=False
        #分数
        self.couse=0
        #子弹
        self.bullets=False#射击信号
        self.bullet_list=[]
        #生命值
        self.Blood=5

    def display(self,l):
        #飞机位置
        self.screen.blit(self.image, self.rect)
        #删除子弹
        #need_del_list=[]#出界的子弹
        for item in self.bullet_list:
            if item.rect.top <0:
                self.bullet_list.remove(item)

        #子弹移动
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move(l)
    #hero重置
    def reset(self):
        if self.life==False:
            self.Blood-=1
            self.rect.center = self.screen_rect.center
            self.rect.bottom = self.screen_rect.bottom

    #敌机重置
    def reMove(self,en1):
        for item in self.bullet_list:
            #print(en1.left, end=' ')
            #print((item.rect.left))
            if (item.rect.left > en1.rect.left)and(item.rect.left< en1.rect.right):
                if(item.rect.top <en1.rect.bottom)and (item.rect.top>en1.rect.top):
                    self.couse+=10
                    en1.reset()
                    self.bullet_list.remove(item)

    def reMove2(self,en2):
        for item in self.bullet_list:
            if (item.rect.left > en2.rect.left)and(item.rect.left< en2.rect.right):#再写一个先判高再判左右
                if(item.rect.top <en2.rect.bottom)and (item.rect.top>en2.rect.top):
                    self.couse+=10
                    en2.reset()
                    self.bullet_list.remove(item)

    def reMove3(self,en3):
        for item in self.bullet_list:
            if (item.rect.left > en3.rect.left ) and (item.rect.left < en3.rect.right):#不在以返回值计算，而是通过传引用计算
                if (item.rect.top < en3.rect.bottom) and (item.rect.bottom > en3.rect.top):
                    self.couse+=10
                    en3.reset()
                    self.bullet_list.remove(item)


    # 飞机移动
    def move_plane(self):
        if self.move_left:
            self.rect.left -=5
            if self.rect.left<-92:
                self.move_left=False
        elif self.move_ringht:
            self.rect.right +=5
            if self.rect.right>579:
                self.move_ringht=False
        elif self.move_up:
            self.rect.top -=3
            if self.rect.top<-50:
                self.move_up=False
        elif self.move_down:
            self.rect.bottom +=5
            if self.rect.bottom>810:
                self.move_down=False
        '''elif self.move_down and self.move_ringht:#放到所有单个条件判断成立前可实现斜飞
            self.rect.bottom +=1
            self.rect.right +=1
            if self.rect.bottom>810:
                self.move_down=False'''
    #射击
    def launch_bullet(self):
        if self.bullets:

            new_bullet = bullet.Bullet(self.rect.left, self.rect.right, self.rect.top, self.rect.bottom, self.screen)
            intn=random.randrange(0,10)
            if intn==3:
            # if intn/2<1:#调整弹速
                self.bullet_list.append(new_bullet)
    def get(self):
        return self.bullet_list

class EnemyPlane(PublicEnemyPlane):
    #敌机1移动
    def __init__(self, screen):
        super().__init__(screen)

        self.image_name = './feiji/a2-2.png'

    def move(self):#左右移动
        if self.direction=='left':
            self.rect.right+=1
            #self.rect.top += 1
            if self.remove == 'True':
                ra = random.randrange(0, 400, 50)
                self.couse+=1
                boom = pygame.image.load(self.boom_image).convert()
                boom_rect = boom.get_rect()
                boom_rect.top = self.rect.top
                boom_rect.left = self.rect.left
                self.rect.right = ra
                self.distion = 'left'
                time.sleep(0.01)
        elif self.direction == 'right':
            self.rect.right -=1
            #self.rect.top +=1
        if self.rect.right>550:
            self.direction='right'
        elif self.rect.right <50:
            self.direction = 'left'
    '''def move(self):#上下移动
        if self.direction=='left':
            self.rect.right+=1
        elif self.direction == 'right':
            self.rect.right -=1
        elif self.direction == 'up':
            self.rect.top +=1
        elif self.direction == 'down':
            self.rect.top -=1

        if self.rect.top >700:
            self.direction = 'down'
        elif self.rect.top<50:
            self.direction = 'up' '''
class EnemyPlane2(PublicEnemyPlane):
    def reset(self):
        ra = random.randrange(0, 400, 50)
        self.couse += 1
        self.rect.right = ra
        rt = -50
        self.couse += 1
        self.rect.top = rt
        self.distion = 'left'
    def move(self):
        if self.direction=='left':
            self.rect.right+=1
            self.rect.top += 1
            if self.rect.top>690:
                self.rect.top=-20

        elif self.direction == 'right':
            self.rect.right -=1
            self.rect.top +=1
            if self.rect.top>690:
                self.rect.top=-20
            if self.remove == 'True':
                ra = random.randrange(0, 400, 50)
                self.couse += 1
                boom = pygame.image.load(self.boom_image).convert()
                boom_rect = boom.get_rect()
                boom_rect.top = self.rect.top
                boom_rect.left = self.rect.left
                self.rect.right = ra
                self.rect.top = 0
                self.distion = 'left'
                time.sleep(0.01)
        if self.rect.right>550:
            self.direction='right'
        elif self.rect.right <50:
            self.direction = 'left'
class EnemyPlane3(PublicEnemyPlane) :
    def __init__(self, screen):
        super().__init__(screen)
        self.Hero=HeroPlane(screen)
        self.direction='left'
    def reset(self):
        ra = random.randrange(0, 400, 50)
        self.couse += 1
        self.rect.right = ra
        rt = -50
        self.couse += 1
        self.rect.top = rt
        self.distion = 'left'
    def move(self):
        if self.direction=='left':
            self.rect.right+=1
            self.rect.top += 1
            if self.rect.top>690:
                self.rect.top=-20
        elif self.direction == 'right':
            self.rect.right -=1
            self.rect.top +=1
            if self.rect.top>690:
                self.rect.top=-20
            if self.remove == 'True':
                ra = random.randrange(0, 400, 50)
                self.couse += 1
                boom = pygame.image.load(self.boom_image).convert()
                boom_rect = boom.get_rect()
                boom_rect.top = self.rect.top
                boom_rect.left = self.rect.left
                self.rect.right = ra
                self.rect.top=0
                self.distion = 'left'
                time.sleep(0.01)
        if self.rect.right>550:
            self.direction='right'
        elif self.rect.right <50:
            self.direction = 'left'