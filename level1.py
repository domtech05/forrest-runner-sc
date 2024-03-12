import pygame


class level1Class:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = False
    def run(self):
        self.running = True
        while self.running:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
            self.clock.tick()
