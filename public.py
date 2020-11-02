import random
import  bullet
import pygame

class PublicEnemyPlane(object):
    remove = False
    def __init__(self,screen):
        # 敌机图
        self.screen = screen
        self.image_name = "./feiji/a2-1.png"
        self.image = pygame.image.load(self.image_name).convert()
        # 获得以及设计敌机坐标
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top
        self.boom_image="./feiji/enemy0_down3.png"
        self.couse=0
        self.bullet_list=[]
        self.blood=5
        self.direction ='right'

    def display(self,hreo):
        self.screen.blit(self.image,self.rect)
        # 存放需要删除的敌机子弹

        for item in self.bullet_list:
            if item.rect.bottom>1000:
                self.bullet_list.remove(item)
            elif (item.rect.bottom>hreo.rect.top)and (item.rect.top<hreo.rect.bottom):
                if (item.rect.left>hreo.rect.left+50)and(item.rect.right<hreo.rect.right-50):
                    hreo.life=False
                    hreo.reset()
                    self.bullet_list.remove(item)

        # 子弹移动
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
    def reset(self):
        ra = random.randrange(0, 400, 50)
        self.couse += 1
        self.rect.right = ra
        self.distion = 'left'
    #敌机1移动
    def move(self):#左右移动
        self.distion = True
        if self.direction=='left':
            self.rect.right+=1
            #self.rect.top += 1
        elif self.direction == 'right':
            self.rect.right -=1
            #self.rect.top +=1
        if self.rect.right>550:
            self.direction='right'
        elif self.rect.right <50:
            self.direction = 'left'
    def move_up_down(self):#上下移动
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
            self.direction = 'up'
    # 敌机射击
    def launch_bullet(self,hero):
        number=random.randint(1,300)
        if number==99:
            new_bullet = bullet.EnBullet(self.rect.left, self.rect.right, self.rect.top, self.rect.bottom, self.screen,hero)
            self.bullet_list.append(new_bullet)
    # def Blood(self):
    #     if self.rect.collidelist(self.herobullet_list):
    #         print(self.herobullet_list)