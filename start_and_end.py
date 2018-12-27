import pygame
import bird


class Title:
    def __init__(self, screen):
        self.screen = screen
        self.x = 150
        self.y = 60
        self.image = pygame.image.load('./image/title.png')

    def display(self):
        self.x -= bird.Bird.b
        self.screen.blit(self.image, (self.x, self.y))


class Startbutton:
    def __init__(self, screen):
        self.screen = screen
        self.x = 300
        self.y = 325
        self.image = pygame.image.load('./image/start.png')

    def display(self):
        self.x -= bird.Bird.b
        self.screen.blit(self.image, (self.x, self.y))


class Tap:
    def __init__(self, screen):
        self.screen = screen
        self.x = 320
        self.y = 200
        self.image = pygame.image.load('./image2/tutorial.png')

    def display(self):

        self.screen.blit(self.image, (self.x, self.y))




