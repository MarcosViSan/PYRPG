import pygame
import player.standingSprite as standingSprite 


MAX_X_VEL = (10, -10)
MAX_Y_VEL = (10, -10)

class Player():

    def __init__(self) -> None:
        self.Colid = {
            'colid-t': 0,
            'colid-b': 0,
            'colid-r': 0,
            'colid-l': 0
        }

        selfColidLines = [] 

        standingSprite.StandingAnimation()
        self.currentAnimation = 'standing'

        standingFrames = ['' for i in range(2)]
        standingFrames[0] = pygame.image.load("assets\\hero-sprites\\1-Pink_Monster\\standing\\standing-1.png")
        standingFrames[1] = pygame.image.load("assets\\hero-sprites\\1-Pink_Monster\\standing\\standing-2.png")

        self.animation = {
            'standing': standingSprite.StandingAnimation(standingFrames),
            'running': 0
        }

        self.xVelocity = 0
        self.yVelocity = 0

    def update(self):
        self.getAnimationState()

    def getAnimationState(self) -> pygame.Surface:
        if (self.xVelocity == 0 and self.yVelocity == 0):
            self.currentAnimation = 'standing'
        elif (self.xVelocity == 0 and self.yVelocity < 0):
            self.currentAnimation = 'falling'
    

        return self.animation[self.currentAnimation].update()
    
    def tryUpVelocity(self, x, y):
        self.xVelocity += x * (int)(not self.Colid['colid-r'])


        self.yVelocity += y * (int)(not self.Colid['colid-t'])