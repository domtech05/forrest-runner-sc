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


def exitButton():  # Create function for use in exit buttons. Allows user to exit the game from within the game
    pygame.quit()
    exit()


class Button: # Create superclass to create buttons within the game
    def __init__(self, text, x, y, bWidth, bHeight, font, imagePath):
        #assign parameters to the buttons (passed in)
        self.text = text
        self.x = x
        self.y = y
        self.width = bWidth
        self.height = bHeight
        self.buttonFont = font

        # Import and display image (path passed in)
        self.buttonImage = pygame.image.load(imagePath)
        self.buttonImage = pygame.transform.scale(self.buttonImage, (self.width, self.height)) # scale button image to fit size



    def draw(self, screen): # create function to draw button to screen
        screen.blit(self.buttonImage, (self.x, self.y)) # show image on screen

        # Render text centered on the button
        text_surface = self.buttonFont.render(self.text, True, (0, 0, 0))
        # centre text to the button image (using the width and height defined)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)



def mainMenu():
    titleFont = pygame.font.Font("FONTS/CabinSketch-Bold.ttf", 100)  # Load font for main title
    taglineFont = pygame.font.Font("FONTS/CabinSketch-Regular.ttf", 50)  # Load font for title taglines

    background_image = pygame.image.load("ASSETS/background.jpg")  # Load background image from assets folder
    background_image = pygame.transform.scale(background_image, (width, height))  # scale background image to fill
    # screen



    class menuButton(Button):
        def __init__(self, text, x, y, width, height, action, font=None):

            buttonFont = pygame.font.Font("FONTS/CabinSketch-Regular.ttf", 60)  # create button font

            # Call the superclass constructor with all the necessary parameters
            super().__init__(text, x, y, width, height, buttonFont, "ASSETS/button.png")

            mouse = pygame.mouse.get_pos()  # get the mouse position on screen and assign it to a variable
            click = pygame.mouse.get_pressed()  # get the click status of the mouse and assign it to a variable
            if x < mouse[0] < x + width and y < mouse[1] < y + height:  # detect if the mouse falls within boundary of
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

        menuButton1 = menuButton("Start", ((width - menuButtonWidth) // 2), (height // 2) - 75, menuButtonWidth,
                                 menuButtonHeight, None)
        menuButton1.draw(screen)

        menuButton2 = menuButton("Settings", ((width - menuButtonWidth) // 2),
                                 ((height // 2) + menuButtonHeight + menuButtonSpacing) - 75, menuButtonWidth,
                                 menuButtonHeight,None)
        menuButton2.draw(screen)

        menuButton3 = menuButton("Exit", ((width - menuButtonWidth) // 2),
                                 ((height // 2) + 2 * (menuButtonHeight + menuButtonSpacing)) - 75, menuButtonWidth,
                                 menuButtonHeight, exitButton)
        menuButton3.draw(screen)

        pygame.display.update()  # draw elements and refresh the display on every clock cycle
        clock.tick(60)  # controls how fast the game clock should run (in this case 60 times per second)


def settingsMenu():
    class DropdownMenu:
        def __init__(self, options, x, y, width, height):
            self.options = options
            self.rect = pygame.Rect(x, y, width, height)
            self.is_open = False

        def draw(self):
            pygame.draw.rect(screen, white, self.rect, 2)  # Draw the dropdown box

            if self.is_open:
                # Draw the dropdown options
                for i, option in enumerate(self.options):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height * (i + 1), self.rect.width,
                                              self.rect.height)
                    pygame.draw.rect(screen, white, option_rect, 2)
                    text_surface = font.render(option, True, black)
                    screen.blit(text_surface, (option_rect.x + 10, option_rect.y + 10))

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.is_open = not self.is_open
                else:
                    self.is_open = False


mainMenu()
