import lib.scene.background as background
import pygame
import lib.player.player as player
import lib.camera as camera
import lib.scene.scene as scene

from pygame.locals import *

FPS = 60
FLAGS = DOUBLEBUF



class gameOrquestrator:
    def __init__(self) -> None:

        pygame.init()
        self.logo = pygame.image.load(".\\assets\\nature-enviroment\PNG\Objects\grass3.png")
        # load and set the logo
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Project RPG")

        self.chunksGroup = []
        self.chunksY = 160

        # create a surface on screen that has the size of 1280 x 720
        self.screen = pygame.display.set_mode((1280 ,720), FLAGS , 8)

        self.font = pygame.font.Font(None, 36)

        self.windowWidth, self.windowHeight = pygame.display.get_window_size()
        
        self.player = player.Player()

        self.fixGround = scene.FixGround()

        self.fixGround.blockArraySize = (int)(self.windowWidth / 576) + 2

        self.camera = camera.Camera((self.windowWidth, self.windowHeight))

        self.background = background.Background()

        self.clock = pygame.time.Clock()

        self.fps = 1


    def main(self):

        # initialize the pygame module
        pygame.init()
        # define a variable to control the main loop
        self.running = True
        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        
        # main loop
        while self.running:
            # event handling, gets all event from the event queue
                self.updatePlayer(pygame.event.get())
                self.updateCamera()
                self.updateScene()
                self.checkColision()
                self.drawScene()
                # self.drawColisors()


                gameInfoText = "FPS: " + (str)((int)(self.fps)) + "   PlayerPOS: " + (str)(self.player.xPos) + "   " + (str)(self.player.yPos) + "    " + (str)(self.player.yMinVelocity) + "   " + (str)(self.player.yVelocity) + "   CamPOS: " + (str)(self.camera.xPos) + "   " + (str)(self.camera.yPos) + "     Chunks: " + str(len(self.chunksGroup))
                
                self.gameInfo = self.font.render(gameInfoText, True, (199, 0, 0))
                
                self.screen.blit(self.gameInfo, (0, 0))

                pygame.display.update()
                self.fps = 1000 / self.clock.tick(FPS)
                print(gameInfoText)

    def drawScene(self):

        for img in range(len(self.background.image)):
            self.screen.blit(self.background.image[img], (0, 0))

        tempXPos = -576

        for i in range(self.fixGround.blockArraySize):
            self.screen.blit(self.fixGround.floorImg, (tempXPos, (self.camera.yPos - self.fixGround.yPos)))
            tempXPos += 576

        for i in range(len(self.chunksGroup)):
            chunkTiles = self.chunksGroup[i].Tiles.sprites()
            for j in range(len(chunkTiles)):
                self.screen.blit(chunkTiles[j].image, (chunkTiles[j].xPos , (self.camera.yPos - chunkTiles[j].yPos)))
                # print(str(chunkTiles[i].xPos) + " " + str(chunkTiles[i].yPos))
                # print('drawed' + str(j)

        self.screen.blit(self.player.image, (self.player.xScreenPos, self.player.yScreenPos))

    def updateScene(self):
        self.fixGround.update()
        
        self.fixGround.xScreenPos = self.fixGround.xPos - self.camera.xPos
        self.fixGround.yScreenPos = self.camera.yPos - self.fixGround.yPos

        if (self.player.yPos >= self.chunksY - 400):
            self.generateChunk()
            # self.destroyChunk()

    def updateCamera(self):
        self.camera.xAcc = 0
        self.camera.yAcc = 0

        if ((self.camera.yPos - self.player.yPos) > self.windowHeight*0.7):
            self.camera.yAcc = -0.5
        elif ((self.camera.yPos - self.player.yPos) < self.windowHeight*0.65):
            self.camera.yAcc = 0.5

        self.camera.update()


    def updatePlayer(self, events):
        self.player.xAcc = 0
        self.player.yAcc = 2

        self.player.xMaxVelocity = 6
        self.player.xMinVelocity = -6


        self.player.yMaxVelocity = 16
        self.player.yMinVelocity = -8 if self.player.preColid['nprecolid-b'] else -2


        self.camera.yMinVelocity = -7.5
        self.camera.yMaxVelocity = 7.5

        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_a] or pressedKeys[pygame.K_LEFT]:
            self.player.xAcc = -2
        elif pressedKeys[pygame.K_d] or pressedKeys[pygame.K_RIGHT]:
            self.player.xAcc = 2
        else:
            self.player.xAcc = 0

        if pressedKeys[pygame.K_SPACE] and self.player.canJump and not self.player.Colid['ncolid-b']:
            self.player.yAcc = 22 if (self.player.yAcc > 4) else 18  
            self.player.canJump = 0
        elif self.player.yAcc > -10:
            self.player.yAcc = -1
    
        for event in events:
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    # change the value to False, to exit the main loop
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.player.canJump = 1

        self.player.update()

        self.player.xScreenPos = self.player.xPos - self.camera.xPos
        self.player.yScreenPos = self.camera.yPos - self.player.yPos

    def checkColision(self):        
        self.player.Colid['ncolid-b'] = 1
        self.player.preColid['nprecolid-b'] = 1

        # print(self.fixGround.colisor)

        # print((str)(self.player.rect.size))

        preColisionFix = self.player.preBCollid.colliderect(self.fixGround.colisor)
        collision = self.player.colidLines["bLine"].colliderect(self.fixGround.colisor)

        print(preColisionFix)
        if (preColisionFix):
            self.player.preColid['nprecolid-b'] = 0
        if (collision):
            self.player.Colid['ncolid-b'] = 0
        else:    
            for Chunk in self.chunksGroup:
                if (self.player.colidLines['bLine'].collidelist(Chunk.TilesColisors) > 0):
                    self.player.Colid['ncolid-b'] = 0
                if (self.player.preBCollid.collidelist(Chunk.TilesColisors) > 0):
                    self.player.preColid['nprecolid-b'] = 0


    def drawColisors(self):
        pygame.draw.rect(self.screen, (0,0,0, 0.2), pygame.rect.Rect(0, 0, 1280, 720))
        pygame.draw.line(self.screen, (190, 0, 0),(self.player.xScreenPos, self.player.yScreenPos + self.player.rect.size[1]), (self.player.xScreenPos + self.player.rect.size[0], self.player.yScreenPos + self.player.rect.size[1]))
        pygame.draw.rect(self.screen, (0, 190, 0), pygame.rect.Rect(self.fixGround.xScreenPos, self.fixGround.yScreenPos, (self.fixGround.blockArraySize * 576), 12))

    def generateChunk(self):

        self.chunksGroup.append(scene.Chunk().genChunk(self.chunksY))
        self.chunksY += 1300

        if (len(self.chunksGroup) > 5):
            self.chunksGroup.pop(0)

