import pygame
from enum import Enum

MAX_X_VEL = (10, -10)
MAX_Y_VEL = (10, -10)

class EnemyLvl1():

    def __init__(self, pos: tuple, fps) -> None:
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

        self.colidLines =  {
            'tLine': pygame.rect.Rect(0,0,0,0),
            'bLine': pygame.rect.Rect(0,0,0,-2),
            'lLine': pygame.rect.Rect(0,0,0,-2),
            'rLine': pygame.rect.Rect(0,0,0,0),
        }

        self.image = None
        self.rect: pygame.rect.Rect = None
        self.xPos = pos[0]
        self.yPos = pos[1] + 100
        self.xAcc = 0
        self.yAcc = 0

        self.rocks = 2200

        self.deathTiming = fps
        
        self.blockChange = False

        self.preBCollid = pygame.rect.Rect(0,0,0,0)

        self.xScreenPos = 0
        self.yScreenPos = 0

        self.xMinVelocity = 0
        self.xMaxVelocity = 0

        self.yMinVelocity = 0

        self.attackCoolDownFull = 0
        self.attackCoolDown = 0

        self.yMaxVelocity = 0

        self.vision = pygame.rect.Rect(0,0,300,200)


        #Propriedades Privadas
        self.currentAnimation = 'standing'

        self.damagingTime = 0

        standingFrames = ['' for i in range(4)]
        standingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\idle\\idle-1.png").convert_alpha(), 2.0)
        standingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\idle\\idle-2.png").convert_alpha(), 2.0)
        standingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\idle\\idle-3.png").convert_alpha(), 2.0)
        standingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\idle\\idle-4.png").convert_alpha(), 2.0)

        # fallingFrames = ['' for i in range(4)]
        # fallingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\falling\\falling-1.png").convert_alpha(), 2.5)
        # fallingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\falling\\falling-2.png").convert_alpha(), 2.5)
        # fallingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\falling\\falling-3.png").convert_alpha(), 2.5)
        # fallingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\falling\\falling-4.png").convert_alpha(), 2.5)

        attackingFrames = ['' for i in range(6)]
        attackingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\attack\\attack-1.png").convert_alpha(), 2.0)
        attackingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\attack\\attack-2.png").convert_alpha(), 2.0)
        attackingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\attack\\attack-3.png").convert_alpha(), 2.0)
        attackingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\attack\\attack-4.png").convert_alpha(), 2.0)
        attackingFrames[4] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\attack\\attack-5.png").convert_alpha(), 2.0)
        attackingFrames[5] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\attack\\attack-6.png").convert_alpha(), 2.0)

        walkingFrames = [ None for i in range(6)]
        walkingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\walking\\walk-1.png").convert_alpha(), 2.0)
        walkingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\walking\\walk-2.png").convert_alpha(), 2.0)
        walkingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\walking\\walk-3.png").convert_alpha(), 2.0)
        walkingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\walking\\walk-4.png").convert_alpha(), 2.0)
        walkingFrames[4] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\walking\\walk-5.png").convert_alpha(), 2.0)
        walkingFrames[5] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\walking\\walk-6.png").convert_alpha(), 2.0)

        deathFrames = ['' for i in range(6)]
        deathFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\death\\death-1.png").convert_alpha(), 2.0)
        deathFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\death\\death-2.png").convert_alpha(), 2.0)
        deathFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\death\\death-3.png").convert_alpha(), 2.0)
        deathFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\death\\death-4.png").convert_alpha(), 2.0)
        deathFrames[4] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\death\\death-5.png").convert_alpha(), 2.0)
        deathFrames[5] = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\2\\death\\death-6.png").convert_alpha(), 2.0)
        
        # jumpingFrames = [ None for i in range(20)]
        # jumpingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-1.png").convert_alpha(), 2.5)
        # jumpingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-2.png").convert_alpha(), 2.5)
        # jumpingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-3.png").convert_alpha(), 2.5)
        # jumpingFrames[3] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-4.png").convert_alpha(), 2.5)
        # jumpingFrames[4] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[5] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[6] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[7] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[8] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[9] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[10] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[11] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[12] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[13] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[14] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[15] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[16] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[17] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[18] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        # jumpingFrames[19] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\jumping\\jumping-5.png").convert_alpha(), 2.5)
        
        # landingFrames = [ None for i in range(3)]
        # landingFrames[0] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\landing\\landing-1.png").convert_alpha(), 2.5)
        # landingFrames[1] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\landing\\landing-2.png").convert_alpha(), 2.5)
        # landingFrames[2] = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\landing\\landing-3.png").convert_alpha(), 2.5)

        self.animation = {
            'standing': StandingAnimation(standingFrames),
            'walking': WalkingAnimation(walkingFrames),
            # 'falling': animationsSprite.WalkingAnimation(fallingFrames),
            # 'jumping': animationsSprite.JumpingAnimation(jumpingFrames),
            # 'landing': animationsSprite.LandingAnimation(landingFrames),
            'attacking': AttackingAnimation(attackingFrames),
            'death': DeathAnimation(deathFrames)
        }

        self.xVelocity = 0
        self.yVelocity = 0
        self.life = 2

        self.canJump = 1
        self.canShoot = 1

    def update(self):
        self.phyAttualize()
        self.move()

        if (self.attackCoolDown > 0): self.attackCoolDown -= 1

        # print(str(self.xPos) + " --- " + str(self.yPos))

        if (self.damagingTime > 0): self.damagingTime -= 1


        self.image, self.rect = self.getAnimationState()
        self.preBCollid.update(self.xPos, (self.yPos - self.rect.size[1] * 0.75),self.rect.size[0], -30)

        self.rect.update(self.xPos, self.yPos, self.rect.width, self.rect.height * -1)


        self.colidLines["bLine"].update(self.xPos + 15, self.yPos - abs(self.rect.size[1]), abs(self.rect.size[0]) - 15, -2)

        if self.motionState == MotionState.death:
            self.deathTiming -= 1


        self.vision.center = self.rect.center
        # print(self.yPos, self.xPos)
        # print(self.yAcc, self.xAcc)
        # print(self.yVelocity, self.xVelocity)
        

        return self

    def getAnimationState(self) -> pygame.Surface:

        if(not self.blockChange):
            if (self.xVelocity == 0 and self.yVelocity == 0 and self.motionState == MotionState.stopped):
                self.currentAnimation = 'standing'
            elif (self.xVelocity != 0 and self.motionState == MotionState.walking):
                self.currentAnimation = 'walking'
            if (self.motionState == MotionState.attacking):
                self.currentAnimation = 'attacking'
            if(self.motionState == MotionState.death):
                self.currentAnimation = 'death'
            if (self.animation[self.currentAnimation].shotKind == animationKind.oneshot): 
                self.animation[self.currentAnimation].finished = False
                self.blockChange = True 

        elif(self.animation[self.currentAnimation].finished):
            self.blockChange = False 
            

        if (self.xVelocity > 0):
            self.direction = "l"
        elif (self.xVelocity < 0):
            self.direction = "r"
        
        if(self.xVelocity == 0):
            if(self.targetPos[0] > self.xPos):
                self.direction = "l"
            elif(self.targetPos[0] < self.xPos):
                self.direction = "r"


    
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
                self.xVelocity += 2
            if(self.xVelocity > 0):
                self.xVelocity += -2
            if(self.xVelocity == -1 or self.xVelocity == 1):
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
    attacking = 4,
    damaging = 5,
    flying = 6,
    landing = 7
    death = 8


import pygame
from enum import Enum

class StandingAnimation(pygame.sprite.Sprite):
       
    def __init__(self, frames):

        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 10
        self.animationItt = 0
        self.shotKind = animationKind.loop 
         
    def update(self, inverted: bool) -> pygame.Surface:        
        if (self.animationItt > self.animationClock):
            self.current += 1
            if self.current == len(self.frames):
                self.current = 0
            self.animationItt = 0

            self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 
        # only needed if size changes within the animation
        self.rect = self.image.get_rect()
        self.animationItt += 1

        return self.image, self.rect

class WalkingAnimation(pygame.sprite.Sprite):
    
    def __init__(self, frames):
        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 3
        self.animationItt = 0
        self.shotKind = animationKind.loop 

         
    def update(self,  inverted: bool) -> pygame.Surface:
        if (self.animationItt > self.animationClock):
            self.current += 1
            if self.current == len(self.frames):
                self.current = 0
            self.animationItt = 0

            self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 
        # only needed if size changes within the animation
        self.rect = self.image.get_rect()
        self.animationItt += 1

        return self.image, self.rect
    

class DeathAnimation(pygame.sprite.Sprite):
    
    def __init__(self, frames):
        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 11
        self.animationItt = 0
        self.shotKind = animationKind.oneshot 

         
    def update(self,  inverted: bool) -> pygame.Surface:
        if (self.animationItt > self.animationClock):
            self.current += 1
            if self.current == len(self.frames):
                self.current = 0
            self.animationItt = 0

            self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 
        # only needed if size changes within the animation
        self.rect = self.image.get_rect()
        self.animationItt += 1

        return self.image, self.rect
    
# class FallingAnimation(pygame.sprite.Sprite):
       
#     def __init__(self, frames):

#         pygame.sprite.Sprite.__init__(self)
#         self.frames = frames       # save the images in here
#         self.current = 0       # idx of current image of the animation
#         self.image = frames[0]  # just to prevent some errors
#         self.rect = self.image.get_rect()    # same here
#         self.playing = 0
#         self.animationClock = 9
#         self.animationItt = 0
#         self.shotKind = animationKind.loop 
         
#     def update(self, inverted: bool) -> pygame.Surface:        
#         if (self.animationItt > self.animationClock):
#             if (self.current < len(self.frames)): self.current += 1
#             # if self.current == len(self.frames):
#             #     self.current = 0
#             self.animationItt = 0

#             self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 


#         # only needed if size changes within the animation
#         self.rect = self.image.get_rect()
#         self.animationItt += 1

#         return self.image, self.rect
    

# class JumpingAnimation(pygame.sprite.Sprite):
       
#     def __init__(self, frames):

#         pygame.sprite.Sprite.__init__(self)
#         self.frames = frames       # save the images in here
#         self.current = 0       # idx of current image of the animation
#         self.image = frames[0]  # just to prevent some errors
#         self.rect = self.image.get_rect()    # same here
#         self.playing = 0
#         self.animationClock = 0 
#         self.animationItt = 0

#         self.shotKind = animationKind.oneshot
         
#         self.finished = False

#     def update(self, inverted: bool) -> pygame.Surface:        
#         if (self.animationItt > self.animationClock):
#             self.current += 1
#             if self.current == len(self.frames):
#                 self.finished = True
#                 self.current = 0
#             self.animationItt = 0

#             self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 
#         # only needed if size changes within the animation
#         self.rect = self.image.get_rect()
#         self.animationItt += 1

#         return self.image, self.rect
    

# class LandingAnimation(pygame.sprite.Sprite):
       
#     def __init__(self, frames):

#         pygame.sprite.Sprite.__init__(self)
#         self.frames = frames       # save the images in here
#         self.current = 0       # idx of current image of the animation
#         self.image = frames[0]  # just to prevent some errors
#         self.rect = self.image.get_rect()    # same here
#         self.playing = 0
#         self.animationClock = 20
#         self.animationItt = 0

#         self.shotKind = animationKind.oneshot
         
#         self.finished = False

#     def update(self, inverted: bool) -> pygame.Surface:        
#         if (self.animationItt > self.animationClock):
#             self.current += 1
#             if self.current == len(self.frames):
#                 self.finished = True
#                 self.current = 0
#             self.animationItt = 0

#             self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 
#         # only needed if size changes within the animation
#         self.rect = self.image.get_rect()
#         self.animationItt += 1

#         return self.image, self.rect
    

class AttackingAnimation(pygame.sprite.Sprite):
       
    def __init__(self, frames):

        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 6
        self.animationItt = 0
        
        self.shotKind = animationKind.oneshot

        self.finished = False
         
    def update(self, inverted: bool) -> pygame.Surface:        
        if (self.animationItt > self.animationClock):
            self.current += 1
            if self.current == len(self.frames):
                self.finished = True
                self.current = 0
            self.animationItt = 0

            self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 
        # only needed if size changes within the animation
        self.rect = self.image.get_rect()
        self.animationItt += 1

        return self.image, self.rect
    

class animationKind(Enum):
    loop = 0
    oneshot = 1