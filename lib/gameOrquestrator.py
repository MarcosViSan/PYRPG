import lib.background as background
import pygame
import lib.player.player as player
import lib.camera as camera
import lib.scene as scene

from pygame.locals import *

FLAGS =FULLSCREEN | DOUBLEBUF


class gameOrquestrator:
    def __init__(self) -> None:

        pygame.init()
        self.logo = pygame.image.load(".\\assets\\nature-enviroment\PNG\Objects\grass3.png")
        # load and set the logo
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Project RPG")

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
        
        # define a variable to control the main loop
        self.running = True
        
        # main loop
        while self.running:
            # event handling, gets all event from the event queue
                self.updatePlayer(pygame.event.get())
                self.updateCamera()
                self.updateScene()
                self.checkColision()
                self.drawScene()
                self.drawColisors()

                gameInfoText = "FPS: " + (str)((int)(self.fps)) + "   PlayerPOS: " + (str)(self.player.xPos) + "   " + (str)(self.player.yPos) + "    " + (str)(self.player.yMaxVelocity) + "   " + (str)(self.player.yVelocity) + "   CamPOS: " + (str)(self.camera.xPos) + "   " + (str)(self.camera.yPos) 
                
                self.gameInfo = self.font.render(gameInfoText, True, (199, 0, 0))
                
                self.screen.blit(self.gameInfo, (0, 0))

                pygame.display.update()
                self.fps = 1000 / self.clock.tick(60)
                print(gameInfoText)

    def drawScene(self):

        for img in range(len(self.background.image)):
            self.screen.blit(self.background.image[img], (0, 0))

        tempXPos = -576

        for i in range(self.fixGround.blockArraySize):
            self.screen.blit(self.fixGround.floorImg, (tempXPos, (self.camera.yPos - self.fixGround.yPos)))
            tempXPos += 576


        self.screen.blit(self.player.image, (self.player.xScreenPos, self.player.yScreenPos))


    def updateScene(self):
        self.fixGround.update()
        
        self.fixGround.xScreenPos = self.fixGround.xPos - self.camera.xPos
        self.fixGround.yScreenPos = self.camera.yPos - self.fixGround.yPos

    def updateCamera(self):
        self.camera.xAcc = 0
        self.camera.yAcc = 0

        if ((self.camera.yPos - self.player.yPos) > self.windowHeight*0.7):
            self.camera.yAcc = -2
        elif ((self.camera.yPos - self.player.yPos) < self.windowHeight*0.65):
            self.camera.yAcc = 2

        self.camera.update()


    def updatePlayer(self, events):
        self.player.xAcc = 0
        self.player.yAcc = 2

        self.player.xMaxVelocity = 3
        self.player.xMinVelocity = -3


        self.player.yMaxVelocity = 6
        self.player.yMinVelocity = -6


        self.camera.yMinVelocity = self.player.yMinVelocity - 1
        self.camera.yMaxVelocity = self.player.yMaxVelocity + 1

        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_a]:
            self.player.xAcc = -2
        elif pressedKeys[pygame.K_d]:
            self.player.xAcc = 2
        else:
            self.player.xAcc = 0

        if pressedKeys[pygame.K_SPACE] and not self.player.Colid['ncolid-b']:
            self.player.yAcc = 8
        elif self.player.yAcc > -10:
            self.player.yAcc = -1
    
        for event in events:
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    # change the value to False, to exit the main loop

        self.player.update()

        self.player.xScreenPos = self.player.xPos - self.camera.xPos
        self.player.yScreenPos = self.camera.yPos - self.player.yPos

    def checkColision(self):        
        self.player.Colid['ncolid-b'] = 1

        print((str)(self.player.rect.size))
        if (self.fixGround.colisor.clipline((self.player.xPos, self.player.yPos - self.player.rect.size[1]), (self.player.xPos + self.player.rect.size[0], self.player.yPos - self.player.rect.size[1]))):
            self.player.Colid['ncolid-b'] = 0

    def drawColisors(self):
        # pygame.draw.rect(self.screen, (0,0,0, 0.2), pygame.rect.Rect(0, 0, 1280, 720))
        pygame.draw.line(self.screen, (190, 0, 0),(self.player.xScreenPos, self.player.yScreenPos + self.player.rect.size[1]), (self.player.xScreenPos + self.player.rect.size[0], self.player.yScreenPos + self.player.rect.size[1]))
        pygame.draw.rect(self.screen, (0, 190, 0), pygame.rect.Rect(self.fixGround.xScreenPos, self.fixGround.yScreenPos, (self.fixGround.blockArraySize * 576), 12))


    



    
        
    


