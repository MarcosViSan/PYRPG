import pygame, random

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

class TileGround(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):

        super().__init__()
        self.xPos = pos[0]
        self.yPos = pos[1]

        self.xScreenPos = 0
        self.yScreenPos = 0

        self.image = pygame.image.load("assets\\nature-enviroment\\PNG\\TileNvl1.png").convert()
        
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.xPos, self.yPos)



class Chunk():
    def __init__(self):
        self.Tiles = pygame.sprite.Group()

    def genChunk(self, initY: int):
        for i in range(8):
            self.Tiles.add(TileGround((random.randint(1, 1136), initY)))
            self.Tiles.add(TileGround((random.randint(1, 1136), initY)))
            initY += 160

        return self