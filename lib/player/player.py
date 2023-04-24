import pygame
import lib.player.animationsSprite as animationsSprite 

MAX_X_VEL = (10, -10)
MAX_Y_VEL = (10, -10)

class Player():

    def __init__(self) -> None:
        #Propriedades acessadas e manipuladas pelo gameCore
        self.Colid = {
            'ncolid-t': 1,
            'ncolid-b': 1,
            'ncolid-r': 1,
            'ncolid-l': 1
        }

        self.direction = "r"

        # self.colidLines =  [None for i in range(4)]
        self.image = None
        self.rect = None
        self.xPos = 500
        self.yPos = 199
        self.xAcc = 0
        self.yAcc = 0

        self.xScreenPos = 0
        self.yScreenPos = 0

        self.xMinVelocity = 0
        self.xMaxVelocity = 0

        self.yMinVelocity = 0
        self.yMaxVelocity = 0


        #Propriedades Privadas
        self.currentAnimation = 'standing'

        standingFrames = ['' for i in range(2)]
        standingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\standing\\standing-1.png").convert_alpha(), 2.5)
        standingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\standing\\standing-2.png").convert_alpha(), 2.5)


        walkingFrames = [ None for i in range(6)]
        walkingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-1.png").convert_alpha(), 2.5)
        walkingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-2.png").convert_alpha(), 2.5)
        walkingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-3.png").convert_alpha(), 2.5)
        walkingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-4.png").convert_alpha(), 2.5)
        walkingFrames[4] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-5.png").convert_alpha(), 2.5)
        walkingFrames[5] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-6.png").convert_alpha(), 2.5
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
            self.xPos += self.xVelocity * self.Colid['ncolid-r']
        elif (self.xVelocity < 0):
            self.xPos += self.xVelocity * self.Colid['ncolid-l']

        if (self.yVelocity < 0):
            self.yPos += self.yVelocity * self.Colid['ncolid-b']
        elif (self.yVelocity > 0):
            self.yPos += self.yVelocity * self.Colid['ncolid-t']


        if (self.xVelocity > 0 and not self.Colid['ncolid-r']):
            self.xVelocity = 0
        elif (self.xVelocity < 0 and not self.Colid['ncolid-l']):
            self.xVelocity = 0
        if (self.yVelocity > 0 and not self.Colid['ncolid-t']):
            self.yVelocity = 0
        elif (self.yVelocity < 0 and not self.Colid['ncolid-b']):
            self.yVelocity = 0
  
    def phyAttualize(self):

        if (self.xVelocity > self.xMinVelocity and self.xAcc < 0):
            self.xVelocity += self.xAcc * self.Colid['ncolid-l']
        elif (self.xVelocity < self.xMaxVelocity and self.xAcc > 0):
            self.xVelocity += self.xAcc * self.Colid['ncolid-r']
        elif (self.xAcc == 0):
            if(self.xVelocity < 0):
                self.xVelocity += 4
            if(self.xVelocity > 0):
                self.xVelocity += -4
            if(self.xVelocity == -2 or self.xVelocity == 2):
                self.xVelocity = 0

        if (self.yVelocity > self.yMinVelocity and self.yAcc < 0):
            self.yVelocity += self.yAcc * self.Colid['ncolid-b']
        elif (self.yVelocity < self.yMaxVelocity and self.yAcc > 0):
            self.yVelocity += self.yAcc * self.Colid['ncolid-t']

        # self.colidLines[0] = pygame.li


        



    