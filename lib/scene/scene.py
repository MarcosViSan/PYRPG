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
        pygame.Surface.set_colorkey(self.image, (0, 0 ,0))
        
        self.rect = self.image.get_rect()

        self.fullRect = self.rect
        # print(self.rect.size)
        self.rect.update(self.xPos, self.yPos, 144, -8)



class Chunk():
    def __init__(self):
        self.Tiles = pygame.sprite.Group()

        self.TilesColisors: list[pygame.rect.Rect] = [pygame.rect.Rect(0,0,0,0)]
        self.FullColisors: list[pygame.rect.Rect] = [pygame.rect.Rect(0,0,0,0)]

        self.chunkTemp = ChunkTemp()

    def genChunk(self, initY: int):

        tilesPos = self.chunkTemp.getBlock(((random.randint(1, 1136), random.randint(1, 1136)), (random.randint(1, 1136), random.randint(1, 1136))))
        for i in range(4):

            tile1 = TileGround((tilesPos[0][0], initY))
            tile2 = TileGround((tilesPos[0][1], initY))
            self.Tiles.add(tile1)
            self.Tiles.add(tile2)

            initY += 160

            tile3 = TileGround((tilesPos[1][0], initY))
            tile4 = TileGround((tilesPos[1][1], initY))
            self.Tiles.add(tile3)
            self.Tiles.add(tile4)

            # print(str(tile1.xPos) + " -- " + str(tile2.xPos))

            self.TilesColisors.append(tile1.rect)
            self.TilesColisors.append(tile2.rect)

            self.FullColisors.append(tile1.fullRect)
            self.FullColisors.append(tile2.fullRect)

            self.TilesColisors.append(tile3.rect)
            self.TilesColisors.append(tile4.rect)

            self.FullColisors.append(tile3.fullRect)
            self.FullColisors.append(tile4.fullRect)
            initY += 160

            tilesPos = self.chunkTemp.getBlock(((tile1.xPos, tile2.xPos), (tile3.xPos, tile4.xPos)))

        return self
    



class ChunkTemp():
    kit1 = [
        ((338,687),(625,800)),((1120,609),
        (1120, 779)), ((236, 1066), (200, 916)),
        ((581, 323),(600, 100)),((1120, 628),
        (900, 671)),((422, 874),(359, 1041)),
        ((1064, 89),(210, 1036)),((299, 846),
        (244, 662)),((536, 144),(65, 410)),
        ((166, 684),(51, 801)),((185, 946),
        (4, 205)),((829, 547),(251, 420)),
        ((234, 554),(414, 193)),((726, 211),
        (880, 78)),((1070, 707),(519, 900)),
        ((212,812),(212,812)),((121,700),
        (269, 913)),((43, 1059), (42, 850)),
        ((229, 89), (264, 47)), ((763, 99),
        (1010, 14)), ((720, 37), (217, 929)),
        ((300, 652), (855, 100)), ((5, 600),
        (221, 623)), ((99, 800), (65, 1058)),
        ((55, 528), (544, 255)), ((421, 10), (100, 590))
    ]

    blackList = []


    def match(self, param: tuple[int, int]):
        for id, item in enumerate(self.kit1):
            try: 
                   if (self.blackList.index(id)): continue
            except Exception as e:
                if ((((abs(param[1][0] - item[0][0]) < 300) or (abs(param[1][0] - item[0][1]) < 300)) and ((abs(param[1][1] - item[0][0]) < 300) or (abs(param[1][1] - item[0][1]) < 300)))):
                    # print(str(e))
                    # print(self.blackList)
                    # print(id)
                    return id
        return -1
    def getBlock(self, param: tuple[tuple, tuple]) -> tuple[tuple, tuple]:
        blockId = self.match(param)
        self.blackList.append(blockId)

        if len(self.blackList) > 8: self.blackList.pop(0)
        return self.kit1[blockId]