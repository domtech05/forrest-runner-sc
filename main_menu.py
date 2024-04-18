"""
Welcome to Forrest Runner source code! Project is programmed in python using pygame (along with other libraries).
This project will form part of my OCR A-Level computer science NEA project. See supporting coursework writeup documents
for more info.

Written by: Dominic H
Candidate number: *REDACTED*
Centre number: *REDACTED*
"""

# import necessary libraries used in program
import pygame
from sys import exit
from level1 import level1Class

class mainMenu:
    def __init__(self):
        pygame.init()
        self.screenWidth = 640
        self.screenHeight = 480
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Forrest Runner')
        self.clock = pygame.time.Clock()
        
        self.titleFont = pygame.font.Font("FONTS/CabinSketch-Bold.ttf", 60)
        self.taglineFont = pygame.font.Font("FONTS/CabinSketch-Regular.ttf", 40)
        self.backgroundImage = pygame.image.load("ASSETS/Images/background.jpg")
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.screenWidth, self.screenHeight))
        
        self.buttons = []
    
    def add_button(self, text, x, y, width, height, action=None):
        buttonFont = pygame.font.Font("FONTS/Pangolin-Regular.ttf", 25)
        button = self.Button(text, x, y, width, height, buttonFont, "ASSETS/button.png", action)
        self.buttons.append(button)
    
    def run(self):
        while True:
            self.handle_events()
            self.draw()
            
            pygame.display.update()
            self.clock.tick(60)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.rect.collidepoint(event.pos):
                        button.clicked = True
                        button.action()
    
    def draw(self):
        self.screen.blit(self.backgroundImage, (0, 0))
        self.screen.blit(self.taglineFont.render("Welcome to", True, (0, 0, 0)),
                         (self.screenWidth // 2 - self.taglineFont.size("Welcome to")[0] // 2, 110))
        self.screen.blit(self.titleFont.render("Forest runner", True, (0, 0, 0)),
                         (self.screenWidth // 2 - self.titleFont.size("Forest runner")[0] // 2, 140))
        
        for button in self.buttons:
            button.draw(self.screen)
    
    class Button:
        def __init__(self, text, x, y, bWidth, bHeight, font, imagePath, action=None):
            self.text = text
            self.x = x
            self.y = y
            self.width = bWidth
            self.height = bHeight
            self.buttonFont = font
            self.clicked = False
            
            self.buttonImage = pygame.image.load(imagePath)
            self.buttonImage = pygame.transform.scale(self.buttonImage, (self.width, self.height))
            
            self.rect = self.buttonImage.get_rect(topleft=(self.x, self.y))
            
            self.action = action
        
        def draw(self, screen):
            screen.blit(self.buttonImage, (self.x, self.y))
            
            textSurface = self.buttonFont.render(self.text, True, (0, 0, 0))
            textRect = textSurface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(textSurface, textRect)
            
    def runLevel(self):
        level1Class(self.screen).run()

if __name__ == "__main__":
    mainMenu = mainMenu()
    mainMenu.add_button("Start", (mainMenu.screenWidth - 150) // 2, (mainMenu.screenHeight // 2) - 30, 150, 40,
                        action=lambda: mainMenu.runLevel())
    mainMenu.add_button("Settings", (mainMenu.screenWidth - 150) // 2, (mainMenu.screenHeight // 2) + 20, 150, 40)
    mainMenu.add_button("Exit", (mainMenu.screenWidth - 150) // 2, (mainMenu.screenHeight // 2) + 70, 150, 40, action=exit)
    
    mainMenu.run()