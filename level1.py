import pygame
from scripts.entities import physicsEntity


# create class to run level 1
class level1Class:
    def __init__(self, screen):
        # create attributes for class
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = False
        self.player = physicsEntity(self, 'player', (50, 50), (8, 15))
        self.movement = [False, False]

    def run(self):  # method to run level 1
        self.running = True  # set running state to true
        while self.running:  # level 1 while loop
            self.player.update((self.movement[1] - self.movement[0], 0))

            for event in pygame.event.get():  # allow user to quit game using OS commands
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                # if loops to detect and use keyboard input to control movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            pygame.display.update()  # update the display and draw all objects to display once per clock cycle
            self.clock.tick(60)  # causes the clock to tick for a set (60) amount of times per second
