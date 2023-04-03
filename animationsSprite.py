import pygame

class StandingAnimation(pygame.sprite.Sprite):
       
    def __init__(self, frames):

        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
         
    def update(self, *args) -> pygame.Surface:
        if self.current == len(self.frames):
            self.current = 0

        self.image = self.frames[self.current]
        # only needed if size changes within the animation
        self.rect = self.image.get_rect(center=self.rect.center)

        return self.image, self.rect

class WalkingAnimation(pygame.sprite.Sprite):
    
    def __init__(self, frames):
        pygame.sprite.Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
         
    def update(self, *args) -> pygame.Surface:
        if self.current == len(self.frames):
            self.current = 0

        self.image = self.frames[self.current]
        # only needed if size changes within the animation
        self.rect = self.image.get_rect(center=self.rect.center)

        return self.image, self.rect