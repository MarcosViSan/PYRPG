import pygame

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

        return self.image, self.rect, False

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

        return self.image, self.rect, False
    
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
         
    def update(self, inverted: bool) -> pygame.Surface:        
        if (self.animationItt > self.animationClock):
            if (self.current < len(self.frames)): self.current += 1
            # if self.current == len(self.frames):
            #     self.current = 0
            self.animationItt = 0

            self.image = pygame.transform.flip(self.frames[self.current], inverted, False) 


        # only needed if size changes within the animation
        self.rect = self.image.get_rect()
        self.animationItt += 1

        return self.image, self.rect, False
    

class JumpingAnimation(pygame.sprite.Sprite):
       
    def __init__(self, frames):

        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        self.animationClock = 16
        self.animationItt = 0
         
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

        return self.image, self.rect, False
    

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

        return self.image, self.rect, not self.finished