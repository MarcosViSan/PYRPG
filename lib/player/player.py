import pygame
import lib.player.animationsSprite as animationsSprite 
from enum import Enum

MAX_X_VEL = (10, -10)
MAX_Y_VEL = (10, -10)

class Player():

    def __init__(self) -> None:
        #Propriedades acessadas e manipuladas pelo gameCore

        self.motionState = MotionState.walking
        self.Colid = {
            'ncolid-t': 1,
            'ncolid-b': 1,
            'ncolid-r': 1,
            'ncolid-l': 1
        }
        self.preColid = {
            'nprecolid-t': 1,
            'nprecolid-b': 1,
            'nprecolid-r': 1,
            'nprecolid-l': 1
        }

        self.direction = "r"
        self.damagingTime = 0

        self.colidLines =  {
            'tLine': pygame.rect.Rect(0,0,0,0),
            'bLine': pygame.rect.Rect(0,0,0,-2),
            'lLine': pygame.rect.Rect(0,0,0,-2),
            'rLine': pygame.rect.Rect(0,0,0,0),
        }

        self.image = None
        self.rect = None
        self.xPos = 500
        self.yPos = 100
        self.xAcc = 0
        self.yAcc = 0

        self.rocks = 2200

        self.life = 3

        self.damageCoolDown = 0

        self.blockChange = False

        self.preBCollid = pygame.rect.Rect(0,0,0,0)

        self.xScreenPos = 0
        self.yScreenPos = 0

        self.xMinVelocity = 0
        self.xMaxVelocity = 0

        self.yMinVelocity = 0
        self.yMaxVelocity = 0


        #Propriedades Privadas
        self.currentAnimation = 'standing'

        self.events = []

        standingFrames = ['' for i in range(2)]
        standingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\standing\\standing-1.png").convert_alpha(), 2.5)
        standingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\standing\\standing-2.png").convert_alpha(), 2.5)

        fallingFrames = ['' for i in range(4)]
        fallingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\falling\\falling-1.png").convert_alpha(), 2.5)
        fallingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\falling\\falling-2.png").convert_alpha(), 2.5)
        fallingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\falling\\falling-3.png").convert_alpha(), 2.5)
        fallingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\falling\\falling-4.png").convert_alpha(), 2.5)

        shootingFrames = ['' for i in range(4)]
        shootingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\shooting\\shooting-1.png").convert_alpha(), 2.5)
        shootingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\shooting\\shooting-2.png").convert_alpha(), 2.5)
        shootingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\shooting\\shooting-3.png").convert_alpha(), 2.5)
        shootingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\shooting\\shooting-4.png").convert_alpha(), 2.5)

        walkingFrames = [ None for i in range(6)]
        walkingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-1.png").convert_alpha(), 2.5)
        walkingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-2.png").convert_alpha(), 2.5)
        walkingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-3.png").convert_alpha(), 2.5)
        walkingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-4.png").convert_alpha(), 2.5)
        walkingFrames[4] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-5.png").convert_alpha(), 2.5)
        walkingFrames[5] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\walking\\walking-6.png").convert_alpha(), 2.5)

        jumpingFrames = [ None for i in range(6)]
        jumpingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-1.png").convert_alpha(), 2.5)
        jumpingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-2.png").convert_alpha(), 2.5)
        jumpingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-3.png").convert_alpha(), 2.5)
        jumpingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-4.png").convert_alpha(), 2.5)
        jumpingFrames[4] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        jumpingFrames[5] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        
        landingFrames = [ None for i in range(3)]
        landingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\landing\\landing-1.png").convert_alpha(), 2.5)
        landingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\landing\\landing-2.png").convert_alpha(), 2.5)
        landingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\landing\\landing-3.png").convert_alpha(), 2.5)

        self.animation: dict[str, any] = {
            'standing': animationsSprite.StandingAnimation(standingFrames),
            'walking': animationsSprite.WalkingAnimation(walkingFrames),
            'falling': animationsSprite.WalkingAnimation(fallingFrames),
            'jumping': animationsSprite.JumpingAnimation(jumpingFrames),
            'landing': animationsSprite.LandingAnimation(landingFrames),
            'shooting': animationsSprite.ShootingAnimation(shootingFrames)
        }

        self.animation['shooting'].eventPoints["shoot"] = 1
        self.animation['jumping'].eventPoints["jump"] = 1
        self.xVelocity = 0
        self.yVelocity = 0

        self.canJump = 1
        self.canShoot = 1

    def update(self):
        self.events.clear()
        # print(self.events)    
        self.phyAttualize()
        self.move()

        self.image, self.rect = self.getAnimationState()

        self.events.extend(self.animation[self.currentAnimation].events)
        self.preBCollid.update(self.xPos, (self.yPos - self.rect.size[1] * 0.75),self.rect.size[0], -30)

        self.colidLines["bLine"].update(self.xPos + 15, self.yPos - self.rect.size[1], self.rect.size[0] - 15, -2)

        self.rect.update(self.xPos, self.yPos, self.rect.width, self.rect.height * -1)

        if (self.damageCoolDown > 0): self.damageCoolDown -= 1

        if (self.damagingTime > 0): self.damagingTime -= 1

        # print(self.damagingTime)

        # print(self.yPos, self.xPos)
        # print(self.yAcc, self.xAcc)
        # print(self.yVelocity, self.xVelocity)
        

        return self

    def getAnimationState(self) -> pygame.Surface:

        if(not self.blockChange):
            if (self.xVelocity == 0 and self.yVelocity == 0 and self.motionState == MotionState.stopped):
                self.currentAnimation = 'standing'
            elif (self.yVelocity != 0 and self.motionState == MotionState.falling):
                self.currentAnimation = 'falling'
            elif (self.xVelocity != 0 and self.motionState == MotionState.walking):
                self.currentAnimation = 'walking'
            elif (self.motionState == MotionState.jumping):
                self.currentAnimation = 'jumping'
            if (self.motionState == MotionState.shooting):
                self.currentAnimation = 'shooting'
            
            if (self.motionState == MotionState.landing):
                self.currentAnimation = "landing"

            if (self.animation[self.currentAnimation].shotKind == animationsSprite.animationKind.oneshot): 
                self.animation[self.currentAnimation].finished = False
                self.blockChange = True 

        elif(self.animation[self.currentAnimation].finished):
            self.blockChange = False 
            

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
        
        if (self.yVelocity < self.yMinVelocity):
            self.yVelocity += 4
            # print("---------------------> " + (str)(self.yVelocity))


        # self.colidLines[0] = pygame.li


class MotionState(Enum):
    stopped = 0,
    walking = 1,
    falling = 2,
    jumping = 3,
    shooting = 4,
    damaging = 5,
    flying = 6,
    landing = 7