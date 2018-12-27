import pygame
import bird


class UP(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("./image/柱子上.png")
        # 定义一个属性，存储图片的矩形信息
        self.rect = self.image.get_rect()
        # 设置这个矩形的左上角
        self.rect.topleft = [self.x, self.y]

    def display(self):
        self.x -= bird.Bird.b
        self.screen.blit(self.image, (self.x, self.y))
        self.rect.topleft = [self.x, self.y]


class DOWN(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("./image/柱子下.png")
        # 定义一个属性，存储图片的矩形信息
        self.rect = self.image.get_rect()
        # 设置这个矩形的左上角
        self.rect.topleft = [self.x, self.y]

    def display(self):
        self.x -= bird.Bird.b
        self.screen.blit(self.image, (self.x, self.y))
        self.rect.topleft = [self.x, self.y]


class Create(object):
    # 储存柱子对象
    lis2 = []

    def __init__(self, screen):
        self.screen = screen
        self.wide = 260
        self.lis = [
            [[800, -180], [800, 312]],
            [[800+self.wide*1, -100], [800+self.wide*1, 382]],
            [[800+self.wide*2, -130], [800+self.wide*2, 352]],
            [[800+self.wide*3, -210], [800+self.wide*3, 482-210]],
            [[800+self.wide*4, -120], [800+self.wide*4, 482-120]],
            [[800+self.wide*5, -270], [800+self.wide*5, 482-270]],
            [[800+self.wide*6, -180], [800+self.wide*6, 482-180]],
            [[800+self.wide*7, -100], [800+self.wide*7, 482-100]],
            [[800+self.wide*8, -130], [800+self.wide*8, 482-130]],
            [[800+self.wide*9, -210], [800+self.wide*9, 482-210]],
            [[800+self.wide*10, -120], [800+self.wide*10, 482-120]],
            [[800+self.wide*11, -270], [800+self.wide*11, 482-270]],
            [[800+self.wide*12, -180], [800+self.wide*12, 482-180]],
            [[800+self.wide*13, -100], [800+self.wide*13, 482-100]],
            [[800+self.wide*14, -130], [800+self.wide*14, 482-130]],
            [[800+self.wide*15, -210], [800+self.wide*15, 482-210]],
            [[800+self.wide*16, -120], [800+self.wide*16, 482-120]],
            [[800+self.wide*17, -270], [800+self.wide*17, 482-270]],
            [[800+self.wide*18, -180], [800+self.wide*18, 482-180]],
            [[800+self.wide*19, -100], [800+self.wide*19, 482-100]],
            [[800+self.wide*20, -130], [800+self.wide*20, 482-130]],
            [[800+self.wide*21, -200], [800+self.wide*21, 482-200]],
            [[800+self.wide*22, -120], [800+self.wide*22, 482-120]],
            [[800+self.wide*23, -270], [800+self.wide*23, 482-270]],
            [[800+self.wide*24, -90], [800+self.wide*24, 482-90]],
        ]

    def cre(self):
        for x in self.lis:
            up1 = UP(self.screen, x[0][0], x[0][1])
            down1 = DOWN(self.screen, x[1][0], x[1][1])
            self.lis2.append([up1, down1])

    def display(self):
        for x in self.lis2:
            if x[0].x < -120:
                del x
            else:
                x[0].display()
                x[1].display()


if __name__ == '__main__':
    pass