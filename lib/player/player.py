import pygame
import lib.player.animationsSprite as animationsSprite 

MAX_X_VEL = (10, -10)
MAX_Y_VEL = (10, -10)

class Player():

    def __init__(self) -> None:
        #Propriedades acessadas e manipuladas pelo gameCore
        self.Colid = {
            'colid-t': 0,
            'colid-b': 0,
            'colid-r': 0,
            'colid-l': 0
        }

        self.direction = "r"

        # self.colidLines =  [None for i in range(4)]
        self.image = None
        self.rect = None
        self.xPos = 10
        self.yPos = 10
        self.xAcc = 0
        self.yAcc = 0
        self.xMinVelocity = 0
        self.xMaxVelocity = 0


        #Propriedades Privadas
        self.currentAnimation = 'standing'

        standingFrames = ['' for i in range(2)]
        standingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\standing\\standing-1.png"), 2.5)
        standingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\standing\\standing-2.png"), 2.5)


        walkingFrames = [ None for i in range(6)]
        walkingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-1.png"), 2.5)
        walkingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-2.png"), 2.5)
        walkingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-3.png"), 2.5)
        walkingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-4.png"), 2.5)
        walkingFrames[4] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-5.png"), 2.5)
        walkingFrames[5] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-6.png"), 2.5
        )

        self.animation = {
            'standing': animationsSprite.StandingAnimation(standingFrames),
            'walking': animationsSprite.WalkingAnimation(walkingFrames),
            'falling': 0
        }

        self.xVelocity = 0
        self.yVelocity = 0

    def update(self):
        self.phyAttualize()
        self.move()
        self.getAnimationState()

        self.image, self.rect = self.getAnimationState()

        # print(self.yPos, self.xPos)
        # print(self.yAcc, self.xAcc)
        # print(self.yVelocity, self.xVelocity)

        return self

    def getAnimationState(self) -> pygame.Surface:
        if (self.xVelocity == 0 and self.yVelocity == 0):
            self.currentAnimation = 'standing'
        elif (self.xVelocity == 0 and self.yVelocity > 0):
            self.currentAnimation = 'standing'
        elif (self.xVelocity != 0):
            self.currentAnimation = 'walking'

        if (self.xVelocity > 0):
            self.direction = "r"
        elif (self.xVelocity < 0):
            self.direction = "l"

    
        # print(self.currentAnimation)
        return self.animation[self.currentAnimation].update(self.direction == "l")
    
    def move(self):
        if (self.xVelocity > 0):
            self.xPos += self.xVelocity * (int)(not self.Colid['colid-r'])
        elif (self.xVelocity < 0):
            self.xPos += self.xVelocity * (int)(not self.Colid['colid-l'])

        if (self.yVelocity > 0):
            self.yPos += self.yVelocity * (int)(not self.Colid['colid-b'])
        elif (self.yVelocity < 0):
            self.yPos += self.yVelocity * (int)(not self.Colid['colid-t'])
  
    def phyAttualize(self):

        if (self.xVelocity > self.xMinVelocity and self.xAcc < 0):
            self.xVelocity += self.xAcc
        elif (self.xVelocity < self.xMaxVelocity and self.xAcc > 0):
            self.xVelocity += self.xAcc
        elif (self.xAcc == 0):
            if(self.xVelocity < 0):
                self.xVelocity += 4
            if(self.xVelocity > 0):
                self.xVelocity += -4
            if(self.xVelocity == -2 or self.xVelocity == 2):
                self.xVelocity = 0

        if (self.yVelocity > -10 and self.yAcc < 0):
            self.yVelocity += self.yAcc
        elif (self.yVelocity < 10 and self.yAcc > 0):
            self.yVelocity += self.yAcc

        # self.colidLines[0] = pygame.li


        



    