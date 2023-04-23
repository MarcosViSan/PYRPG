import pygame

class FixGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.xPos = 0
        self.yPos = 0

        self.xScreenPos = 0
        self.yScreenPos = 0

        self.blockArraySize = 0

        self.floorImg = pygame.image.load("assets\\nature-enviroment\\PNG\\FixGround.png").convert_alpha()

        self.colisor = pygame.rect.Rect(0, 0, 0, 0)

    def update(self):
       self.colisor.update(self.xPos, self.yPos, (self.blockArraySize * 576), 10)
