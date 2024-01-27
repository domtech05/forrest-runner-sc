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
screen = pygame.display.set_mode(
    (width, height))  # sets the display size for pygame to render to (in this case # 1920*1080)
pygame.display.set_caption('Forrest Runner')  # sets window title show to user within host OS

clock = pygame.time.Clock()  # Creates a clock variable that is constantly updated during execution. Used to control


# all time dependant functions within the game.


# Create function that will allow user to exit game from host OS.
def exitFunc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def mainMenu():
    titleFont = pygame.font.Font("CabinSketch-Bold.ttf", 100)  # Load font for main title
    taglineFont = pygame.font.Font("CabinSketch-Regular.ttf", 50)  # Load font for title taglines

    background_image = pygame.image.load("ASSETS/background.jpg")  # Load background image from assets folder
    background_image = pygame.transform.scale(background_image, (width, height))  # scale background image to fill

    # screen

    # Function to draw buttons to the screen
    class menuButton:
        def __init__(self, text, x, y, bWidth, bHeight):
            self.text = text
            self.x = x
            self.y = y
            self.width = bWidth
            self.height = bHeight

            self.buttonImage = pygame.image.load("ASSETS/button.png")
            self.buttonImage = pygame.transform.scale(self.buttonImage, (self.width, self.height))
            self.buttonFont = pygame.font.Font("CabinSketch-Regular.ttf", 45)

        def draw(self, screen):
            screen.blit(self.buttonImage, (self.x, self.y))

            # Render text centered on the button
            text_surface = self.buttonFont.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(text_surface, text_rect)


    # Main menu loop
    while True:
        # allow user to exit from the game from the OS
        exitFunc()

        screen.blit(background_image, (0, 0))  # Draw background image to screen

        screen.blit(taglineFont.render("Welcome to", True, (0, 0, 0)),
                    (width // 2 - taglineFont.size("Welcome to")[0] // 2, 290))  # Add tagline to top of title
        screen.blit(titleFont.render("Forest runner", True, (0, 0, 0)),
                    (width // 2 - titleFont.size("Forest runner")[0] // 2, 320))  # Draw main title to screen

        button_width, button_height = 200, 50
        button_start_y = height // 2
        button = menuButton("Click Me", ((width // 2) - (button_width // 2)), button_start_y - 10, button_width, button_height)
        button.draw(screen)

        pygame.display.update()  # draw elements and refresh the display on every clock cycle
        clock.tick(60)  # controls how fast the game clock should run (in this case 60 times per second)


mainMenu()
