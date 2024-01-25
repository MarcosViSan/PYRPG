import pygame
import math

class Rock(pygame.sprite.Sprite):
    def __init__(self, catAdj, catOpp, pxPos, pyPos):
        pygame.sprite.Sprite.__init__(self)

        self.yPos = pyPos
        self.xPos = pxPos

        # print(catAdj, catOpp)

        self.trajetory = math.sqrt(math.pow(catAdj, 2) + math.pow(catOpp, 2))

        self.yVelocity = 0
        self.xVelocity = 0
        
        self.xAcc = 14 * (catAdj / self.trajetory)
        self.yAcc = 14 * (catOpp / self.trajetory)

        # print(self.xAcc)
        # print(self.yAcc)


        print(catAdj, catOpp, self.trajetory)

        self.xMinVelocity = -(14 * (catAdj / self.trajetory))
        self.xMaxVelocity = (14 * (catAdj / self.trajetory))

        self.yMinVelocity = -(14 * (catOpp / self.trajetory))
        self.yMaxVelocity = (14 * (catOpp / self.trajetory))

        self.image = pygame.transform.scale_by(pygame.image.load("assets\\hero-sprites\\Pink_Monster\\Rock1.png"), 2.5)
        self.rect = self.image.get_rect()

        self.rect.update(self.xPos, self.yPos, self.rect.width, self.rect.height * -1)

    def update(self):
        self.xPos += self.xVelocity

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
        # self.rect.move_ip(self.xPos, self.yPos)

        self.rect.x, self.rect.y = self.xPos, self.yPos
        
        if (self.yVelocity < self.yMinVelocity):
            self.yVelocity = self.yMinVelocity
        if (self.xVelocity < self.xMinVelocity):
            self.xVelocity = self.xMinVelocity

        if (self.yVelocity > self.yMaxVelocity):
            self.yVelocity = self.yMaxVelocity
        if (self.xVelocity > self.xMaxVelocity):
            self.xVelocity = self.xMaxVelocity

        if (self.yVelocity < self.yMaxVelocity):
            self.yVelocity -= 2
        if (self.xVelocity < self.xMaxVelocity):
            self.xVelocity -= 2

        # print(self.xVelocity, self.yVelocity)
        



class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self, catAdj, catOpp, pxPos, pyPos):
        pygame.sprite.Sprite.__init__(self)

        self.yPos = pyPos
        self.xPos = pxPos

        # print(catAdj, catOpp)

        self.trajetory = math.sqrt(abs(math.pow(catAdj, 2) + math.pow(catOpp, 2)))

        self.yVelocity = 0
        self.xVelocity = 0
        
        self.xAcc = 10 * (catAdj / self.trajetory)
        self.yAcc = 10 * (catOpp / self.trajetory)

        # print(self.xAcc)
        # print(self.yAcc)


        # print(catAdj, catOpp, self.trajetory)

        self.xMinVelocity = -abs(10 * (catAdj / self.trajetory))
        self.xMaxVelocity = abs(10 * (catAdj / self.trajetory))

        self.yMinVelocity = -abs(10 * (catOpp / self.trajetory))
        self.yMaxVelocity = abs(10 * (catOpp / self.trajetory))

        self.image = pygame.transform.scale_by(pygame.image.load("assets\\enemies-sprites\\3\\Projectile.png"), 2.5)
        self.rect = self.image.get_rect()

        self.rect.update(self.xPos, self.yPos, self.rect.width, self.rect.height)

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
        # self.rect.move_ip(self.xPos, self.yPos)

        self.rect.x, self.rect.y = self.xPos, self.yPos
        
        if (self.yVelocity < self.yMinVelocity):
            self.yVelocity += 2
        if (self.xVelocity < self.xMinVelocity):
            self.xVelocity += 2

        if (self.yVelocity < self.yMaxVelocity):
            self.yVelocity -= 2
        if (self.xVelocity < self.xMaxVelocity):
            self.xVelocity -= 2