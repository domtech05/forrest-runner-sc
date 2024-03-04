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
screen = pygame.display.set_mode((width, height))  # sets the display size for pygame to render to (in this case
                                                    # 1920*1080)
pygame.display.set_caption('Forrest Runner')  # sets window title show to user within host OS

clock = pygame.time.Clock()  # Creates a clock variable that is constantly updated during execution. Used to control


# all time dependant functions within the game.


# Create function that will allow user to exit game from host OS.
def exitFunc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def exitButton():  # Create function for use in exit buttons. Allows user to exit the game from within the game
    pygame.quit()
    exit()


class Button: # Create superclass to create buttons within the game
    def __init__(self, text, x, y, bWidth, bHeight, font, imagePath):
        # assign parameters to the buttons (passed in)
        self.text = text
        self.x = x
        self.y = y
        self.width = bWidth
        self.height = bHeight
        self.buttonFont = font
        self.clicked = False

        # Import and display image (path passed in)
        self.buttonImage = pygame.image.load(imagePath)
        self.buttonImage = pygame.transform.scale(self.buttonImage, (self.width, self.height)) # scale button
        # image to fit button size

        # Create a rect attribute for collision detection
        self.rect = self.buttonImage.get_rect(topleft=(self.x, self.y))



    def draw(self, screen): # create function to draw button to screen
        # Update the rect attribute to reflect the current position
        self.rect.topleft = (self.x, self.y)

        screen.blit(self.buttonImage, (self.x, self.y)) # show image on screen

        # Render text centered on the button
        textSurface = self.buttonFont.render(self.text, True, (0, 0, 0))
        # centre text to the button image (using the width and height defined)
        textRect = textSurface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(textSurface, textRect)



def mainMenu():
    titleFont = pygame.font.Font("FONTS/CabinSketch-Bold.ttf", 100)  # Load font for main title
    taglineFont = pygame.font.Font("FONTS/CabinSketch-Regular.ttf", 50)  # Load font for title taglines

    backgroundImage = pygame.image.load("ASSETS/background.jpg")  # Load background image from assets folder
    backgroundImage = pygame.transform.scale(backgroundImage, (width, height))  # scale background image to fill
    # screen



    class menuButton(Button):
        def __init__(self, text, x, y, width, height, action):
            buttonFont = pygame.font.Font("FONTS/CabinSketch-Regular.ttf", 60)
            super().__init__(text, x, y, width, height, buttonFont, "ASSETS/button.png")
            self.action = action
            self.clicked = False

        def checkClick(self):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if self.rect.collidepoint(mouse):  # Use the rect attribute from the superclass
                if click[0] == 1 and self.action is not None:
                    self.clicked = True
                    self.action()


    menuButtonSpacing = 30  # define the space between each menu button
    menuButtonHeight, menuButtonWidth = 75, 350  # define the size for each button
    # Use the button class to show the three buttons on screen
    menuButton1 = menuButton("Start", ((width - menuButtonWidth) // 2), (height // 2) - 75, menuButtonWidth,
                             menuButtonHeight, None)

    menuButton2 = menuButton("Settings", ((width - menuButtonWidth) // 2),
                             ((height // 2) + menuButtonHeight + menuButtonSpacing) - 75, menuButtonWidth,
                             menuButtonHeight, settingsMenu)

    menuButton3 = menuButton("Exit", ((width - menuButtonWidth) // 2),
                             ((height // 2) + 2 * (menuButtonHeight + menuButtonSpacing)) - 75, menuButtonWidth,
                             menuButtonHeight, exitButton)


    # Main menu loop
    while True:
        # allow user to exit from the game from the OS
        exitFunc()

        screen.blit(backgroundImage, (0, 0))  # Draw background image to screen

        screen.blit(taglineFont.render("Welcome to", True, (0, 0, 0)),
                    (width // 2 - taglineFont.size("Welcome to")[0] // 2, 290))  # Add tagline to top of title
        screen.blit(titleFont.render("Forest runner", True, (0, 0, 0)),
                    (width // 2 - titleFont.size("Forest runner")[0] // 2, 320))  # Draw main title to screen


        menuButton1.checkClick()
        menuButton2.checkClick()
        menuButton3.checkClick()
        if menuButton1.clicked or menuButton2.clicked or menuButton3.clicked:
            break


        menuButton1.draw(screen)
        menuButton2.draw(screen)
        menuButton3.draw(screen)


        pygame.display.update()  # draw elements and refresh the display on every clock cycle
        clock.tick(60)  # controls how fast the game clock should run (in this case 60 times per second)



    while True:
        exitFunc()

        # Draw everything
        screen.fill((255, 255, 255))
        dropdown_menu.draw()


        pygame.display.update()
        clock.tick(60)


mainMenu()
