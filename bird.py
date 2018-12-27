import pygame
from pygame.locals import *
import time
import pillar
import time


class Bird(pygame.sprite.Sprite):
    b = 0

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = 130
        self.y = 250
        self.screen = screen
        self.image_5 = pygame.image.load("./image/bird-5.png")
        self.image_4 = pygame.image.load("./image/bird-4.png")
        self.image_3 = pygame.image.load("./image/bird-3.png")
        self.image_2 = pygame.image.load("./image/bird-2.png")
        self.image_1 = pygame.image.load("./image/bird-1.png")
        self.image = pygame.image.load("./image/bird0.png")
        self.image0 = pygame.image.load("./image/bird0.png")
        self.image1 = pygame.image.load("./image/bird1.png")
        self.image2 = pygame.image.load("./image/bird2.png")
        self.image3 = pygame.image.load("./image/bird3.png")
        self.image4 = pygame.image.load("./image/bird4.png")
        self.down_speed = 0  # 当前速度
        self.add_speed = 0  # 重力加速度 默认1
        self.time = 0  # 上次跳的时间
        self.jump_time = 0.2  # 每次跳之间的间隔
        # 定义一个属性，存储图片的矩形信息
        self.rect = self.image.get_rect()
        # 设置这个矩形的左上角
        self.rect.topleft = [self.x, self.y]
        self.start_flag = False

    def jump(self):
        self.y += self.down_speed  # 下落
        if self.down_speed < 10:  # 控制速度极限
            self.down_speed += self.add_speed  # 加速度
        # 键盘检测
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE and self.start_flag is True:
                    Bird.b = 2.2  # 让柱子和背景开始移动
                    if time.time() > self.time + self.jump_time:
                        self.add_speed = 0.6  # 第一次设置加速度
                        self.down_speed = -10  # 每次跳的高度
                        self.time = time.time()
            elif event.type == pygame.MOUSEBUTTONDOWN and 300 <= event.pos[0] <= 300+170 and\
                    325 <= event.pos[1] <= 325+95 and self.start_flag is False:
                self.start_flag = True
                Bird.b = 0.7
            if event.type == MOUSEBUTTONDOWN and self.start_flag is True:
                Bird.b = 2.2  # 让柱子和背景开始移动
                if time.time() > self.time + self.jump_time:
                    self.add_speed = 0.6  # 第一次设置加速度
                    self.down_speed = -10  # 每次跳的高度
                    self.time = time.time()

    def display(self):
        if -8 >= self.down_speed:
            self.screen.blit(self.image4, (self.x, self.y))
        elif -8 <= self.down_speed <= -6:
            self.screen.blit(self.image3, (self.x, self.y))
        elif -6 <= self.down_speed <= -4:
            self.screen.blit(self.image2, (self.x, self.y))
        elif -4 <= self.down_speed <= -2:
            self.screen.blit(self.image1, (self.x, self.y))
        elif -2 <= self.down_speed <= 1:
            self.screen.blit(self.image0, (self.x, self.y))
        elif 1 <= self.down_speed <= 3.3:
            self.screen.blit(self.image_1, (self.x, self.y))
        elif 3.3 <= self.down_speed <= 5.4:
            self.screen.blit(self.image_2, (self.x, self.y))
        elif 5.4 <= self.down_speed <= 7.7:
            self.screen.blit(self.image_3, (self.x, self.y))
        elif self.down_speed >= 7.7:
            self.screen.blit(self.image_4, (self.x, self.y))
        self.rect.topleft = [self.x, self.y]

    def check_die(self, bird):
        if self.y > 425:
            exit()
        if self.y < 0:
            self.y = 0
        for pillars in pillar.Create.lis2:
            for x in pillars:
                if pygame.sprite.collide_mask(bird, x):
                    Bird.b = 0
                    self.start_flag = False
                    self.image = self.image_2
                    self.display()
                    self.image = self.image_5


if __name__ == '__main__':
    Bird(1)
