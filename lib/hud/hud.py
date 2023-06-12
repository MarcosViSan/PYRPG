import pygame
class HudinGame():
    def __init__(self, screenSize: tuple):
        self.screen = pygame.surface.Surface(screenSize)

        self.screen.set_colorkey((0,0,0))

        self.opened = False

        print(str(self.screen.get_width()))

        self.options = [
            Option("Continuar", (self.screen.get_width()*0.425, self.screen.get_height()*0.400), 0),
            Option("Restart", (self.screen.get_width()*0.425, self.screen.get_height()*0.500), 1),
            Option("Menu", (self.screen.get_width()*0.425, self.screen.get_height()*0.600), 2),
            Option("Sair", (self.screen.get_width()*0.425, self.screen.get_height()*0.700), 3),
        ]

    def update(self):

        mousePos = pygame.mouse.get_pos()

        self.screen.fill((0,0,0))

        for option in self.options:
            if option.rect.collidepoint(mousePos):
                option.hover = True
            else:
                option.hover = False
            
            if option.hover and option.size < option.maxSize:
                option.size += 4
            elif not option.hover and option.size > option.minSize:
                option.size -= 4

            self.writeText(option.text, (190, 225, 255), (option.xPos, option.yPos), option.size)
    



    def writeText(self,text, fontColor, coord: tuple, fontSiz: int = 20, border = True, borderColor: tuple = (1,1,1)):

        font = pygame.font.Font("assets\\hero-sprites\\Font\\Planes_ValMore.ttf", fontSiz)
        texto_renderizado = font.render(text, True, borderColor)
        self.screen.blit(texto_renderizado, (coord[0] - 2, coord[1] - 2))  # Desenha a borda
        self.screen.blit(texto_renderizado, (coord[0] + 2, coord[1] - 2))  # Desenha a borda
        self.screen.blit(texto_renderizado, (coord[0] - 2, coord[1] + 2))  # Desenha a borda
        self.screen.blit(texto_renderizado, (coord[0] + 2, coord[1] + 2))  # Desenha a borda

        # Renderização do texto
        texto_renderizado = font.render(text, True, fontColor)
        self.screen.blit(texto_renderizado, coord) 


class Option():
    def __init__(self, text, pos, val):
        self.text = text
        self.yPos = pos[1]
        self.xPos = pos[0]

        self.val = val
        self.hover = False

        self.rect = pygame.rect.Rect(self.xPos, self.yPos, 300, 25)

        self.size = 24
        self.maxSize = 40
        self.minSize = 24
