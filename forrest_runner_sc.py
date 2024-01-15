"""
Welcome to Forrest Runner source code! Project is programmed in python using pygame (along with other libraries).
This project will form part of my OCR A-Level computer science NEA project. See supporting coursework writeup documents.

Written by: Dominic H
Candidate number: 9626
Centre number: 18517
"""

#import necessary libraries used in program
import pygame
import time as t

#setup pygame and create window for game to run in
pygame.init()

DS1 = pygame.display.set_mode((2560,1440))

while True:
    
    #allow user to exit from the game from the OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            
    pygame.display.update() #draw elements and refresh the display