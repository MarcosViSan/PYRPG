import lib.background as background
import pygame
import lib.player.player as player

class gameCore:
    def __init__(self) -> None:

        pygame.init()
        self.logo = pygame.image.load(".\\assets\\nature-enviroment\PNG\Objects\grass3.png")
        # load and set the logo
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Project RPG")

        # create a surface on screen that has the size of 1280 x 720
        self.screen = pygame.display.set_mode((1280 ,720))

        self.player = player.Player()

        self.background = background.Background()

        self.clock = pygame.time.Clock()


    def main(self):

        # initialize the pygame module
        
        # define a variable to control the main loop
        self.running = True

        self.drawBackground()
        self.drawScene()
        
        # main loop
        while self.running:
            # event handling, gets all event from the event queue
                self.update(pygame.event.get())
                self.clock.tick(1)

    def drawBackground(self):
        for img in range(len(self.background.image)):
            self.screen.blit(self.background.image[img], (0, 0))
            pygame.display.flip()

    def drawScene(self):
        floor = ['' for i in range(3)]
        floor[0] = pygame.image.load(".\\assets\\nature-enviroment\\PNG\\Tiles\\tile23.png")
        floor[1] = pygame.image.load(".\\assets\\nature-enviroment\\PNG\\Tiles\\tile22.png")
        floor[2] = pygame.image.load(".\\assets\\nature-enviroment\\PNG\\Tiles\\tile24.png")

        subFloor = ['' for i in range(3)]
        subFloor[0] = pygame.image.load(".\\assets\\nature-enviroment\\PNG\\Tiles\\tile118.png")
        subFloor[1] = pygame.image.load(".\\assets\\nature-enviroment\\PNG\\Tiles\\tile11.png")
        subFloor[2] = pygame.image.load(".\\assets\\nature-enviroment\\PNG\\Tiles\\tile39.png")

        windowSize = pygame.display.get_window_size()
        xFloorPos = 0
        yFloorPos = windowSize[1]*0.8
        for i in range(9):
            for j in range(len(floor)):
                self.screen.blit(floor[j], (xFloorPos, yFloorPos))
                xFloorPos += 48

        xSubFloorPos = 0
        ySubFloorPos = yFloorPos + 48
        for j in range(3):
            for i in range(27):
                self.screen.blit(subFloor[j], (xSubFloorPos, ySubFloorPos))
                xSubFloorPos += 48
            ySubFloorPos += 48

        pygame.display.flip()


    def setColisors(self):
        windowWidth, windowHeight = pygame.display.get_window_size()
        self.groundColisor = pygame.Rect(0, windowHeight*0.8, windowWidth, 48)


    def update(self, events):
        player.xAcc = 0
        player.yAcc = 2
        for event in events:
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    # change the value to False, to exit the main loop
                if event.type == pygame.K_a:
                    player.xAcc = -2
                elif event.type == pygame.K_d:
                    player.xAcc = 2

                if event.type == pygame.K_SPACE:
                    player.yAcc = -8
                elif player.yAcc < 10:
                    player.yAcc += 2
        
        self.drawPlayer(self.player.update())


    def drawPlayer(self, player):
        self.screen.blit(player.image, (player.xPos, player.yPos))
