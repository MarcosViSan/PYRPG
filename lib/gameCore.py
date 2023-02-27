import lib.background as background
import pygame

class gameCore:
    def __init__(self) -> None:

        pygame.init()
        self.logo = pygame.image.load(".\\assets\\nature-enviroment\PNG\Objects\grass3.png")
        # load and set the logo
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Project RPG")

        # create a surface on screen that has the size of 1280 x 720
        self.screen = pygame.display.set_mode((1280 ,720))

        self.background = background.Background()


    def main(self):

        # initialize the pygame module
        
        # define a variable to control the main loop
        running = True

        self.drawBackground()
        
        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

    def drawBackground(self):
        for img in range(len(self.background.image)):
            self.screen.blit(self.background.image[img], (0, 0))
            pygame.display.flip()
