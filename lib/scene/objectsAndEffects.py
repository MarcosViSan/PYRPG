import pygame

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        self.yPos = 0
        self.xPos = 0

        self.yVelocity = 0
        self.xVelocity = 0
        
        self.xAcc = 0
        self.yAcc = 0

        self.xMinVelocity = 0
        self.xMaxVelocity = 0

        self.yMinVelocity = 16
        self.yMaxVelocity = 16

    def update(self):
        if (self.yVelocity > self.yMinVelocity and self.yAcc < 0):
            self.yVelocity += self.yAcc
        elif (self.yVelocity < self.yMaxVelocity and self.yAcc > 0):
            self.yVelocity += self.yAcc
        
        if (self.yVelocity < self.yMinVelocity):
            self.yVelocity += 4
