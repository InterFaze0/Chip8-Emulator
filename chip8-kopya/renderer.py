import pygame

class Renderer:


    def __init__(self):
        self.cols = 64
        self.rows = 32
        self.display = [0] * 2150 #TODO renderer.py fix
        
        
        self.pixelSize = 10
        self.screen = pygame.display.set_mode((700,400))
        pygame.init()

    def drawScreenPixels(self,l):
        counter = 0
        for y in range(20,340,10):
            for x in range(30,670,10):
                if l[counter] == 1:
                    pixel = pygame.Rect(x,y,self.pixelSize,self.pixelSize)
                    pygame.draw.rect(self.screen,(175,215,70),pixel)
                elif l[counter] == 0:
                    pixel = pygame.Rect(x,y,self.pixelSize,self.pixelSize)
                    pygame.draw.rect(self.screen,("#3c3c3b"),pixel)  
                counter += 1
    

    def setPixel(self,x,y):
        if (x > self.cols):
            x -= self.cols
        elif (x < 0):
            x += self.cols
        
        if (y > self.rows):
            y -= self.rows
        elif (y < 0):
            y += self.rows
        
        pixelLoc = x + (y * self.cols)
        self.display[pixelLoc] ^= 1
        return not self.display[pixelLoc]
    
    def clear(self):
        self.display = [0] * 2150
    
    def render(self):
        self.screen.fill("#3c3c3b")
        self.drawScreenPixels(self.display)
        pygame.display.flip()
