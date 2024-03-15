import pygame


# create class to run level 1
class level1Class:
    def __init__(self, screen):
        # create attributes for class
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self): # method to run level 1
        self.running = True # set running state to true
        while self.running: # level 1 while loop

            for event in pygame.event.get(): # allow user to quit game using OS commands
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update() # update the display and draw all objects to display once per clock cycle
            self.clock.tick(60) # causes the clock to tick for a set (60) amount of times per second
