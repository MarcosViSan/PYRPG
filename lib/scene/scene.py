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
       self.colisor.update(self.xPos, self.yPos, (self.blockArraySize * 576), -10)

class TileGround(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):

        super().__init__()
        self.xPos = pos[0]
        self.yPos = pos[1]

        self.xScreenPos = 0
        self.yScreenPos = 0

        self.image = pygame.image.load("assets\\nature-enviroment\\PNG\\TileNvl1.png").convert()
        
        self.rect = self.image.get_rect()
        # print(self.rect.size)
        self.rect.update(self.xPos, self.yPos, 144, -8)



class Chunk():
    def __init__(self):
        self.Tiles = pygame.sprite.Group()

        self.TilesColisors: list[pygame.rect.Rect] = [pygame.rect.Rect(0,0,0,0)]

    def genChunk(self, initY: int):
        for i in range(8):

            tile1 = TileGround((random.randint(1, 1136), initY))
            tile2 = TileGround((random.randint(1, 1136), initY))
            self.Tiles.add(tile1)
            self.Tiles.add(tile2)

            self.TilesColisors.append(tile1.rect)
            self.TilesColisors.append(tile2.rect)
            initY += 160

        return self