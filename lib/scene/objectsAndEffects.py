import pygame
import math

class Rock(pygame.sprite.Sprite):
    def __init__(self, catAdj, catOpp, pxPos, pyPos):
        pygame.sprite.Sprite.__init__(self)

        self.yPos = pyPos
        self.xPos = pxPos

        self.trajetory = math.sqrt(abs(math.pow(catAdj, 2) + math.pow(catOpp, 2)))

        self.yVelocity = 0
        self.xVelocity = 0
        
        self.xAcc = math.ceil(10 * (catAdj / self.trajetory)) 
        self.yAcc = math.ceil(10 * (catOpp / self.trajetory))

        # print(catAdj, catOpp, self.trajetory)

        self.xMinVelocity = -abs(math.ceil(10 * (catAdj / self.trajetory))) 
        self.xMaxVelocity = abs(math.ceil(10 * (catAdj / self.trajetory)))

        self.yMinVelocity = -abs(math.ceil(10 * (catOpp / self.trajetory)))
        self.yMaxVelocity = abs(math.ceil(10 * (catOpp / self.trajetory)))

        self.image = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\Rock1.png"), 2.5)
        self.rect = self.image.get_rect()

    def update(self):
        if (self.xVelocity != 0):
            self.xPos += self.xVelocity

        if (self.yVelocity != 0):
            self.yPos += self.yVelocity

        if (self.yVelocity > self.yMinVelocity and self.yAcc < 0):
            self.yVelocity += self.yAcc
        elif (self.yVelocity < self.yMaxVelocity and self.yAcc > 0):
            self.yVelocity += self.yAcc

        if (self.xVelocity > self.xMinVelocity and self.xAcc < 0):
            self.xVelocity += self.xAcc
        elif (self.xVelocity < self.xMaxVelocity and self.xAcc > 0):
            self.xVelocity += self.xAcc

        # print(self.rect.size)
        self.rect.move_ip(self.xPos, self.yPos)
        
        if (self.yVelocity < self.yMinVelocity):
            self.yVelocity += 2
        if (self.xVelocity < self.xMinVelocity):
            self.xVelocity += 2

        if (self.yVelocity < self.yMaxVelocity):
            self.yVelocity -= 2
        if (self.xVelocity < self.xMaxVelocity):
            self.xVelocity -= 2

        # print(self.xVelocity, self.yVelocity)

