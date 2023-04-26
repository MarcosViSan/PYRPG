class Camera():

    def __init__(self, windowSize):

        self.yPos = windowSize[1]
        self.xPos = 0

        self.yVelocity = 0
        self.xVelocity = 0

        
        self.yMinVelocity = 0
        self.yMaxVelocity = 0

        self.xAcc = 0
        self.yAcc = 0



    def update(self):

        if (self.yVelocity > self.yMinVelocity and self.yAcc < 0):
            self.yVelocity += self.yAcc
        elif (self.yVelocity < self.yMaxVelocity and self.yAcc > 0):
            self.yVelocity += self.yAcc
        elif (self.xAcc == 0):
            if(self.yVelocity < 0):
                self.yVelocity += 3
            if(self.yVelocity > 0):
                self.yVelocity += -3
            if(self.yVelocity >= -2 or self.yVelocity <= 2):
                self.yVelocity = 0

        self.xPos += self.xVelocity
        self.yPos += self.yVelocity

