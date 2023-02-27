import pygame

class Background:
    def __init__(self) -> None:
        self.image = ['' for i in range(5)]
        self.image[0] = pygame.image.load(".\\assets\\backgrounds\m3\\1.png") 
        self.image[1] = pygame.image.load(".\\assets\\backgrounds\m3\\2.png") 
        self.image[2] = pygame.image.load(".\\assets\\backgrounds\m3\\3.png") 
        self.image[3] = pygame.image.load(".\\assets\\backgrounds\m3\\4.png") 
        self.image[4] = pygame.image.load(".\\assets\\backgrounds\m3\\5.png") 
