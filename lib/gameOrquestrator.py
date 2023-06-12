import lib.scene.background as background
import pygame
import lib.player.player as player
import lib.enemies.enemies as enemies
import lib.camera as camera
import lib.hud.hud as hud
import lib.scene.objectsAndEffects as objFx
import lib.scene.scene as scene
import random

from pygame.locals import *

FPS = 60
FLAGS = DOUBLEBUF



class gameOrquestrator:
    def __init__(self) -> None:


        pygame.init()
        pygame.font.init()
        self.logo = pygame.image.load(".\\assets\\nature-enviroment\PNG\Objects\grass3.png")
        # load and set the logo
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Project RPG")

        self.chunksGroup = []
        self.chunksY = 160
        self.target = [0,0]


        self.effectsAndObjects = {
            "Rocks": [],
            "Lazer": []
        }

        self.damageArea = [pygame.rect.Rect(0,0,0,0)]

        self.enemies = []

        # create a surface on screen that has the size of 1280 x 720
        self.finalScreen = pygame.display.set_mode((1280 ,720), FLAGS , 8)
        self.gameScreen = pygame.surface.Surface(pygame.display.get_window_size())

        self.windowWidth, self.windowHeight = pygame.display.get_window_size()
        self.hudInGame = hud.HudinGame((self.windowWidth, self.windowHeight))
        
        self.player = player.Player()

        self.fixGround = scene.FixGround()

        self.fixGround.blockArraySize = (int)(self.windowWidth / 576) + 2

        self.camera = camera.Camera((self.windowWidth, self.windowHeight))

        self.background = background.Background()

        self.clock = pygame.time.Clock()

        self.fps = 1

        self.gameover = False

        self.looseArea = pygame.rect.Rect(0, self.camera.yPos - 1440, 1280, 80)


    def main(self):

        # initialize the pygame module
        pygame.init()
        # define a variable to control the main loop
        self.running = True
        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        
        # main loop
        while self.running:
            # event handling, gets all event from the event queue
                # self.update()
            events = pygame.event.get()
            self.fps = 1000 / self.clock.tick(FPS)

            self.handleNoGame(events)

            if not self.gameover and not self.hudInGame.opened:
                self.updatePlayer(events)
                self.updateCamera()
                self.updateScene()
                self.updateEnemies()
                self.updateObjectsAndEffects()
                self.checkColision()
                self.drawScene()
                self.drawObjectsAndEffects()
                # self.drawColisors()

                gameInfoText = "FPS: " + (str)((int)(self.fps)) + "   PlayerPOS: " + (str)(self.player.xPos) + "   " + (str)(self.player.yPos) + "    " + (str)(self.player.yMinVelocity) + "   " + (str)(self.player.yVelocity) + "   CamPOS: " + (str)(self.camera.xPos) + "   " + (str)(self.camera.yPos) + "     Chunks: " + str(len(self.chunksGroup)) + "   Enemies: " + str(len(self.enemies)) + " life " + str(self.player.life)
                   
                self.writeText(gameInfoText, (255, 255, 255), (0, 0), 24)
                self.finalScreen.blit(self.gameScreen, (0, 0))

                   # print(gameInfoText)
                if self.player.life <= 0: self.gameover = True 
            elif self.gameover:
                self.gameScreen.fill((1,1,1))
                self.writeText("Game Over", (255, 190, 190), (self.windowWidth*0.425, self.windowHeight/2), 35, True, (50, 50, 50)) 
                self.finalScreen.blit(self.gameScreen, (0, 0))
            
            if self.hudInGame.opened:
                self.hudInGame.update()
                self.finalScreen.blit(pygame.transform.grayscale(self.gameScreen), (0, 0))
                self.finalScreen.blit(self.hudInGame.screen, (0, 0))
                
            pygame.display.update()

    def handleNoGame(self, events):
            for event in events:
                # only do something if the event is of type QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.hudInGame.opened = not self.hudInGame.opened 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                # change the value to False, to exit the main loop

    def drawScene(self):

        for img in range(len(self.background.image)):
            self.gameScreen.blit(self.background.image[img], (0, 0))

        tempXPos = -576

        for i in range(self.fixGround.blockArraySize):
            self.gameScreen.blit(self.fixGround.floorImg, (tempXPos, (self.camera.yPos - self.fixGround.yPos)))
            tempXPos += 576

        for i in range(len(self.chunksGroup)):
            chunkTiles = self.chunksGroup[i].Tiles.sprites()
            for j in range(len(chunkTiles)):
                self.gameScreen.blit(chunkTiles[j].image, (chunkTiles[j].xPos , (self.camera.yPos - chunkTiles[j].yPos)))
                # print(str(chunkTiles[i].xPos) + " " + str(chunkTiles[i].yPos))
                # print('drawed' + str(j)
        self.drawEnemies()

        if(self.player.damagingTime > 0): self.player.image.fill((255,0,0), special_flags=pygame.BLEND_MULT)
        
        self.gameScreen.blit(self.player.image, (self.player.xScreenPos, self.player.yScreenPos))

    def drawObjectsAndEffects(self):
        for item in self.effectsAndObjects["Rocks"]:
            self.screen.blit(item.image, (item.xPos, (self.camera.yPos - item.yPos)))

    def drawEnemies(self):
        for item in self.enemies:
            if(item.damagingTime > 0): item.image.fill((255,0,0), special_flags=pygame.BLEND_MULT)
            self.gameScreen.blit(item.image, (item.xPos, (self.camera.yPos - item.yPos)))

    def updateScene(self):
        self.fixGround.update()
        
        self.fixGround.xScreenPos = self.fixGround.xPos - self.camera.xPos
        self.fixGround.yScreenPos = self.camera.yPos - self.fixGround.yPos

        if (self.player.yPos >= self.chunksY - 400):
            self.generateChunk()
            # self.destroyChunk()

    def updateObjectsAndEffects(self):
        for item in self.effectsAndObjects["Rocks"]:
            item.update()

            keep = False

            for enemy in self.enemies:
                if item.rect.colliderect(enemy.rect):
                    self.effectsAndObjects["Rocks"].remove(item)
                    enemy.life -= 1
                    enemy.damagingTime = FPS * 0.15
                    keep = True
                    break

            if keep: continue
            
            for Chunk in self.chunksGroup:
                if (item.rect.collidelist(Chunk.FullColisors) > 0):
                    self.effectsAndObjects["Rocks"].remove(item)
            

    def updateCamera(self):
        self.camera.xAcc = 0
        self.camera.yAcc = 0

        if ((self.camera.yPos - self.player.yPos) > self.windowHeight*0.7 and self.camera.yPos - self.looseArea.y > 720):
            self.camera.yAcc = -0.5
        elif ((self.camera.yPos - self.player.yPos) < self.windowHeight*0.65):
            self.camera.yAcc = 0.5

        self.camera.update()


    def updatePlayer(self, events):
        self.player.xAcc = 0
        self.player.yAcc = -2

        mousePos = pygame.mouse.get_pos()

        # print(mousePos)

        self.targetPos = (mousePos[0] - self.camera.xPos, self.camera.yPos - mousePos[1])

        self.player.xMaxVelocity = 6
        self.player.xMinVelocity = -6


        self.player.yMaxVelocity = 16
        self.player.yMinVelocity = -8 if self.player.preColid['nprecolid-b'] else -2


        self.camera.yMinVelocity = -7.5
        self.camera.yMaxVelocity = 7.5

        pressedKeys = pygame.key.get_pressed()

        if (pressedKeys[pygame.K_a] or pressedKeys[pygame.K_LEFT]):
            self.player.xAcc = -2
            if (self.player.yVelocity == 0): self.player.motionState = player.MotionState.walking
        elif (pressedKeys[pygame.K_d] or pressedKeys[pygame.K_RIGHT]):
            self.player.xAcc = 2
            if (self.player.yVelocity == 0): self.player.motionState = player.MotionState.walking
        else:
            self.player.xAcc = 0
            self.player.motionState = player.MotionState.stopped
        if pressedKeys[pygame.K_SPACE] and self.player.canJump and not self.player.Colid['ncolid-b']:
            self.player.yAcc = 22 if (self.player.yAcc > 4) else 18  
            self.player.canJump = 0
            self.player.motionState = player.MotionState.jumping
        elif self.player.yAcc > -10:
            self.player.yAcc = -1

        if (self.player.yVelocity < 0): self.player.motionState = player.MotionState.falling
    
        for event in events:
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    # change the value to False, to exit the main loop
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.player.canJump = 1

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.player.rocks > 0 and len(self.effectsAndObjects["Rocks"]) < 500:
                    self.effectsAndObjects["Rocks"].append(objFx.Rock(self.targetPos[0] - self.player.xPos, self.targetPos[1] - self.player.yPos, self.player.xPos, self.player.yPos)) 
                    if (self.targetPos[0] < self.player.xPos): self.player.direction = "l"
                    if (self.targetPos[0] > self.player.xPos): self.player.direction = "r"
                    self.player.motionState = player.MotionState.shooting
                    self.player.canShoot = 1

        self.player.update()

        if (self.player.xPos > 1280): self.player.xPos = -40
        elif (self.player.xPos < -40): self.player.xPos = 1280

        self.player.xScreenPos = self.player.xPos - self.camera.xPos
        self.player.yScreenPos = self.camera.yPos - self.player.yPos

    def checkColision(self):        
        self.player.Colid['ncolid-b'] = 1
        self.player.preColid['nprecolid-b'] = 1

        for item in self.enemies:
            item.Colid['ncolid-b'] = 1
            item.preColid['nprecolid-b'] = 1

        if (self.player.rect.colliderect(self.looseArea)): self.player.life = 0

        # print(self.fixGround.colisor)

        # print((str)(self.player.rect.size))

        preColisionFix = self.player.preBCollid.colliderect(self.fixGround.colisor)
        collision = self.player.colidLines["bLine"].colliderect(self.fixGround.colisor)

        if (self.player.rect.collidelist(self.damageArea) > 0 and self.player.damageCoolDown == 0):
            self.player.life -= 1
            self.player.damageCoolDown = FPS * 1.5
            # self.player.motionState = player.MotionState.damaging
            self.player.damagingTime = FPS * 0.15
        
        self.damageArea.clear()
        self.damageArea = [pygame.rect.Rect(0,0,0,0)]        
        

        # print(preColisionFix)
        if (preColisionFix):
            self.player.preColid['nprecolid-b'] = 0
        if (collision):
            self.player.Colid['ncolid-b'] = 0
            self.player.motionState = player.MotionState.landing

        for Chunk in self.chunksGroup:
            if (self.player.colidLines['bLine'].collidelist(Chunk.TilesColisors) > 0):
                self.player.Colid['ncolid-b'] = 0
                self.player.motionState = player.MotionState.landing
            if (self.player.preBCollid.collidelist(Chunk.TilesColisors) > 0):
                self.player.preColid['nprecolid-b'] = 0

            for item in self.enemies:
                if (item.colidLines['bLine'].collidelist(Chunk.TilesColisors) > 0):
                    item.Colid['ncolid-b'] = 0
                if (item.preBCollid.collidelist(Chunk.TilesColisors) > 0):
                    item.preColid['nprecolid-b'] = 0


    def drawColisors(self):
        pygame.draw.rect(self.gameScreen, (0,0,0, 0.2), pygame.rect.Rect(0, 0, 1280, 720))
        pygame.draw.line(self.gameScreen, (190, 0, 0),(self.player.xScreenPos, self.player.yScreenPos + self.player.rect.size[1]), (self.player.xScreenPos + self.player.rect.size[0], self.player.yScreenPos + self.player.rect.size[1]))
        pygame.draw.rect(self.gameScreen, (0, 190, 0), pygame.rect.Rect(self.fixGround.xScreenPos, self.fixGround.yScreenPos, (self.fixGround.blockArraySize * 576), 12))

    def generateChunk(self):

        self.chunksGroup.append(scene.Chunk().genChunk(self.chunksY))
        self.chunksY += 1280

        self.looseArea.y += 700

        if (len(self.chunksGroup) > 3):
            self.chunksGroup.pop(0)
        
        self.generateEnemies()

    def generateEnemies(self):
        chunk = self.chunksGroup[len(self.chunksGroup) - 1]

        tiles = chunk.Tiles.sprites()

        tile = tiles[random.randint(0, 1)]

        self.enemies.append(enemies.EnemyLvl1(tile.fullRect.center, FPS))

        tile = tiles[random.randint(2, 3)]

        self.enemies.append(enemies.EnemyLvl1(tile.fullRect.center, FPS))

        if(len(self.enemies) > 9): self.enemies.pop(0)


    def updateEnemies(self):
        for item in self.enemies:

            if (item.rect != None):
                distanceToPlayer = abs(pygame.Vector2.distance_to(pygame.Vector2(item.rect.center), pygame.Vector2(self.player.rect.center)))

            item.attackCoolDownFull = FPS * 1.5
        
            item.xAcc = 0
            item.yAcc = -2

            # print(mousePos)

            item.targetPos = (self.player.xPos, self.player.yPos)

            item.xMaxVelocity = 3
            item.xMinVelocity = -3

            if(item.vision.collidepoint(self.player.xPos, self.player.yPos)):
                if (distanceToPlayer > 80 and item.targetPos[0] < item.xPos):
                    item.xAcc = -1
                    item.motionState = enemies.MotionState.walking
                
                if (distanceToPlayer > 80 and item.targetPos[0] > item.xPos):
                    item.xAcc = 1
                    item.motionState = enemies.MotionState.walking
            else:
                item.xAcc = 0
                item.motionState = enemies.MotionState.stopped

            if (item.rect != None):
                if((distanceToPlayer < 80) and item.attackCoolDown == 0):
                    item.attackCoolDown = item.attackCoolDownFull 
                    item.motionState = enemies.MotionState.attacking
                if (item.direction == "l"):
                    self.damageArea.append(pygame.rect.Rect(item.xPos + item.rect.width, item.yPos - 25, 20, 30))
                elif (item.direction == "r"):
                    self.damageArea.append(pygame.rect.Rect(item.xPos - item.rect.width*0.7, item.yPos - 25, 20, 30))


            item.yMaxVelocity = 16
            item.yMinVelocity = -8 if item.preColid['nprecolid-b'] else -2

            if item.life < 1: 
                item.motionState = enemies.MotionState.death
                if item.deathTiming < 1:
                    self.enemies.remove(item)

            item.update()
            # for Chunk in self.chunksGroup:
                    # if (item.rect.collidelist(Chunk.FullColisors) > 0):
                    #     self.enemies.remove(item)


    def writeText(self,text, fontColor, coord: tuple, fontSiz: int = 20, border = True, borderColor: tuple = (0,0,0)):

        font = pygame.font.Font("assets\\hero-sprites\\Font\\Planes_ValMore.ttf", fontSiz)
        texto_renderizado = font.render(text, True, (0,0,0))
        self.gameScreen.blit(texto_renderizado, (coord[0] - 2, coord[1] - 2))  # Desenha a borda
        self.gameScreen.blit(texto_renderizado, (coord[0] + 2, coord[1] - 2))  # Desenha a borda
        self.gameScreen.blit(texto_renderizado, (coord[0] - 2, coord[1] + 2))  # Desenha a borda
        self.gameScreen.blit(texto_renderizado, (coord[0] + 2, coord[1] + 2))  # Desenha a borda

        # Renderização do texto
        texto_renderizado = font.render(text, True, fontColor)
        self.gameScreen.blit(texto_renderizado, coord) 