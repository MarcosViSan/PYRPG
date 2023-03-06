import lib.gameCore as gameCore
# define a main function
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    game = gameCore.gameCore()
    game.main()
    

