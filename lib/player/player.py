import pygame
import player.standingSprite as standingSprite 

class Player():

    def __init__(self) -> None:
        pass

    def load(self):
        standingFramesFull = pygame.image.load(".\\assets\\hero-sprites\\1-Pink_Monster\\Pink_Monster_Idle_4.png")
        standingFrames = []
        self.standing = standingSprite.StandingAnimation()