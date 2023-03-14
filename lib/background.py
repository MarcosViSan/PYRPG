import pygame

class Background:
    def __init__(self) -> None:
        self.image = ['' for i in range(5)]
        self.image[0] = pygame.transform.scale(pygame.image.load(".\\assets\\background\m3\\1.png"), (1280 ,720)) 
        self.image[1] = pygame.transform.scale(pygame.image.load(".\\assets\\background\m3\\2.png"), (1280 ,720)) 
        self.image[2] = pygame.transform.scale(pygame.image.load(".\\assets\\background\m3\\3.png"), (1280 ,720)) 
        self.image[3] = pygame.transform.scale(pygame.image.load(".\\assets\\background\m3\\4.png"), (1280 ,720)) 
        self.image[4] = pygame.transform.scale(pygame.image.load(".\\assets\\background\m3\\5.png"), (1280 ,720)) 
        
