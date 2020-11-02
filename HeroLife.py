import pygame
pygame.init()
class lifePlane(object):
    def __init__(self, screen):
        self.select_image = './feiji/plane.png'
        self.background_game = pygame.image.load(self.select_image).convert()
        # 获得以及设计飞机坐标
        self.rect = self.background_game.get_rect()
        self.screen=screen
        self.rect.left = 400
        self.rect.top = 0

    def display(self):
        #飞机位置
        self.screen.blit(self.background_game, self.rect)