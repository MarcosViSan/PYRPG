from ast import Dict
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
        self.animationClock = 17
        self.animationItt = 0
        self.shotKind = animationKind.loop 

        self.eventPoints: dict[str, int] = {}
        self.events = []
         
    def update(self, inverted: bool) -> pygame.Surface:   
        self.events.clear()
     
        if (self.animationItt > self.animationClock):
            for event in self.eventPoints.keys():
                if self.current == self.eventPoints[event]:
                    self.events.append(event)
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
        self.eventPoints: dict[str, int] = {}
        self.events = []

         
    def update(self,  inverted: bool) -> pygame.Surface:

        self.events.clear()
        if (self.animationItt > self.animationClock):
            for event in self.eventPoints.keys():
                if self.current == self.eventPoints[event]:
                    self.events.append(event)
            self.current += 1
            if self.current == len(self.frames):
                self.current = 0
            self.animationItt = 0

            self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 
        # only needed if size changes within the animation
        self.rect = self.image.get_rect()

        self.animationItt += 1

        return self.image, self.rect
    
class FallingAnimation(pygame.sprite.Sprite):
       
    def __init__(self, frames):

        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 9
        self.animationItt = 0
        self.shotKind = animationKind.loop
        self.eventPoints: dict[str, int] = {}
        self.events = []
         
    def update(self, inverted: bool) -> pygame.Surface:  
        self.events.clear()
        if (self.animationItt > self.animationClock):
            for event in self.eventPoints.keys():
                if self.current == self.eventPoints[event]:
                    self.events.append(event)
            if (self.current < len(self.frames)): self.current += 1
            # if self.current == len(self.frames):
            #     self.current = 0
            self.animationItt = 0

            self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 

        # only needed if size changes within the animation
        self.rect = self.image.get_rect()
        self.animationItt += 1

        return self.image, self.rect
    

class JumpingAnimation(pygame.sprite.Sprite):
       
    def __init__(self, frames):

        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 3
        self.animationItt = 0

        self.shotKind = animationKind.oneshot
         
        self.finished = False
        self.eventPoints: dict[str, int] = {}
        self.events = []

    def update(self, inverted: bool) -> pygame.Surface:        
        self.events.clear()
        if (self.animationItt > self.animationClock):
            for event in self.eventPoints.keys():
                if self.current == self.eventPoints[event]:
                    self.events.append(event)
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
    

class LandingAnimation(pygame.sprite.Sprite):
       
    def __init__(self, frames):

        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 20
        self.animationItt = 0

        self.shotKind = animationKind.oneshot
         
        self.finished = False
        self.eventPoints: dict[str, int] = {}
        self.events = []

    def update(self, inverted: bool) -> pygame.Surface:   
        self.events.clear()
        if (self.animationItt > self.animationClock):
            for event in self.eventPoints.keys():
                if self.current == self.eventPoints[event]:
                    self.events.append(event)
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
    

class ShootingAnimation(pygame.sprite.Sprite):
       
    def __init__(self, frames):

        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 4
        self.animationItt = 0
        self.eventPoints: dict[str, int] = {}
        self.events = []
        
        self.shotKind = animationKind.oneshot

        self.finished = False
         
    def update(self, inverted: bool) -> pygame.Surface:  
        self.events.clear()  
        if (self.animationItt > self.animationClock):
            for event in self.eventPoints.keys():
                if self.current == self.eventPoints[event]:
                    self.events.append(event)
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