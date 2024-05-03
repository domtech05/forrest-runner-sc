import pygame
import os


class gameOver():
    def __init__(self):
        pygame.init()
        pygame.init()  # initialise pygame to be able to use its functions

        # define and create screen to render objects to
        self.screenWidth = 640
        self.screenHeight = 480
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Forrest Runner')

        # Create a clock variable that is constantly updated during execution of the program
        self.clock = pygame.time.Clock()

        self.gameOverFont = pygame.font.Font("FONTS/CabinSketch-Bold.ttf", 60)

        self.backgroundImage = pygame.image.load("ASSETS/Images/background.jpg")
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.screenWidth, self.screenHeight))

        self.buttons = []

    def add_button(self, text, x, y, width, height, action=None):  # function to set up variables for buttons
        buttonFont = pygame.font.Font("FONTS/Pangolin-Regular.ttf", 25)
        button = self.Button(text, x, y, width, height, buttonFont, "ASSETS/button.png", action)
        self.buttons.append(button)

    def run(self):  # Main function to run the main menu
        while True:
            self.handle_events()
            self.draw()

            pygame.display.update()  # update display and render objects
            self.clock.tick(60)  # sets clock tick rate for program

    def handle_events(self):  # Event detection for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.rect.collidepoint(event.pos):
                        button.clicked = True
                        button.action()

    def draw(self):  # render all text and images to screen
        self.screen.blit(self.backgroundImage, (0, 0))
        self.screen.blit(self.gameOverFont.render("GAME OVER!", True, (0, 0, 0)),
                         (self.screenWidth // 2 - self.gameOverFont.size("Welcome to")[0] // 2, 110))

        for button in self.buttons:
            button.draw(self.screen)

    class Button:  # class to create and render buttons to the screen
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

        def draw(self, screen):  # draw buttons to screen
            screen.blit(self.buttonImage, (self.x, self.y))

            textSurface = self.buttonFont.render(self.text, True, (0, 0, 0))
            textRect = textSurface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(textSurface, textRect)

    def runMenu(self):  # run level 1 when start is pressed
        os.system('py main_menu.py')
        exit()


if __name__ == "__main__":
    gameOver = gameOver()
    gameOver.add_button("Main menu", (gameOver.screenWidth - 150) // 2, (gameOver.screenHeight // 2) - 30, 150, 40,
                        action=lambda: gameOver.runMenu())
    gameOver.add_button("Exit", (gameOver.screenWidth - 150) // 2, (gameOver.screenHeight // 2) + 20, 150, 40, action=exit)

    gameOver.run()
