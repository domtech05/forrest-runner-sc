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

# setup pygame and create window for game to run in
pygame.init()  # initialize all pygame modules to avoid having initialize all separately
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))  # sets the display size for pygame to render to (in this case 1920*1080)
pygame.display.set_caption('Forrest Runner')  # sets window title show to user within host OS

clock = pygame.time.Clock()  # Creates a clock variable that is constantly updated during execution. Used to control
# all time dependant functions within the game.


# FONT AND TEXT SETUP
fontRegular = pygame.font.Font("CabinSketch-Regular.ttf", 20)  # define a regular size font to be used through the game
fontBold = pygame.font.Font("CabinSketch-Bold.ttf", 20)  # define a bold font to be used for titles


# Create function that will allow user to exit game from host OS. Must be called in every while loop!!
def exitFunc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def mainMenu():
    titleFont = pygame.font.Font("CabinSketch-Bold.ttf", 100)
    while True:
        # allow user to exit from the game from the OS
        exitFunc()

        screen.fill((255, 255, 255))  # TEMP
        screen.blit(titleFont.render("Forest runner", True, (0, 0, 0)), ((width / 2), (height / 2)))  # TEMP

        pygame.display.update()  # draw elements and refresh the display on every clock cycle
        clock.tick(60)  # controls how fast the game clock should run (in this case 60 times per second)


mainMenu()
