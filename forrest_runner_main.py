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

def exitButton():
    pygame.quit()
    exit()



def mainMenu():
    titleFont = pygame.font.Font("CabinSketch-Bold.ttf", 100)  # Load font for main title
    taglineFont = pygame.font.Font("CabinSketch-Regular.ttf", 50)  # Load font for title taglines

    background_image = pygame.image.load("ASSETS/background.jpg")  # Load background image from assets folder
    background_image = pygame.transform.scale(background_image, (width, height))  # scale background image to fill
    # screen


    # Function to draw buttons to the screen
    def drawMenuButton(text, x, y, bWidth, bHeight, action):
        buttonImage = pygame.image.load("ASSETS/button.png")  # load button image
        buttonImage = pygame.transform.scale(buttonImage, (
            bWidth, bHeight))  # scale button image to be correct size according to parameter passed in
        buttonFont = pygame.font.Font("CabinSketch-Regular.ttf", 60)  # create button font

        screen.blit(buttonImage, (x, y))  # draw the button image to the screen

        # Render text
        text_surface = buttonFont.render(text, True, (0, 0, 0))  # render the text according to parameter passed in
        text_rect = text_surface.get_rect(center=(x + bWidth // 2, y + bHeight // 2))  # centre text to the button image
        screen.blit(text_surface, text_rect)  # draw the text to the screen

        # Click actions
        mouse = pygame.mouse.get_pos()  # get the mouse position on screen and assign it to a variable
        click = pygame.mouse.get_pressed()  # get the click status of the mouse and assign it to a variable

        if x < mouse[0] < x + bWidth and y < mouse[1] < y + bHeight:  # detect if the mouse falls within boundary of
            # the button
            if click[0] == 1 and action is not None:  # detect if mouse is clicked
                action()  # run action defined in function parameter


    # Main menu loop
    while True:
        # allow user to exit from the game from the OS
        exitFunc()

        screen.blit(background_image, (0, 0))  # Draw background image to screen

        screen.blit(taglineFont.render("Welcome to", True, (0, 0, 0)),
                    (width // 2 - taglineFont.size("Welcome to")[0] // 2, 290))  # Add tagline to top of title
        screen.blit(titleFont.render("Forest runner", True, (0, 0, 0)),
                    (width // 2 - titleFont.size("Forest runner")[0] // 2, 320))  # Draw main title to screen

        menuButtonSpacing = 30  # define the space between each menu button
        menuButtonHeight, menuButtonWidth = 75, 350  # define the size for each button

        drawMenuButton("Start", ((width - menuButtonWidth) // 2), (height // 2) - 75, menuButtonWidth, menuButtonHeight,
                       None)  # draw the start button to the screen

        drawMenuButton("Settings", ((width - menuButtonWidth) // 2),
                       ((height // 2) + menuButtonHeight + menuButtonSpacing) - 75, menuButtonWidth, menuButtonHeight,
                       None)  # draw the settings button to the screen

        drawMenuButton("Exit", ((width - menuButtonWidth) // 2),
                       ((height // 2) + 2 * (menuButtonHeight + menuButtonSpacing)) - 75, menuButtonWidth,
                       menuButtonHeight, exitButton)  # draw the exit button to the screen

        pygame.display.update()  # draw elements and refresh the display on every clock cycle
        clock.tick(60)  # controls how fast the game clock should run (in this case 60 times per second)


mainMenu()