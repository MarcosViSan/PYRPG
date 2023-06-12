import lib.gameOrquestrator as gameOrquestrator
import pygame
# define a main function
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    game = gameOrquestrator.GameOrquestrator()
    pygame.init()

    while game.running:
        game.main(pygame.event.get())

        if game.restart: 
            del game
            game = gameOrquestrator.GameOrquestrator()