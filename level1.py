import pygame
from scripts.entities import physicsEntity
from scripts.utils import loadImage, bulkImageLoad
from scripts.tilemap1 import tilemap


# create class to run level 1
class level1Class:
    def __init__(self, screen):
        # create attributes for class
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.movement = [False, False]
        
        self.assets = {
            'decor': bulkImageLoad('tiles/decor'),
            'grass': bulkImageLoad('tiles/grass'),
            'largeDecor': bulkImageLoad('tiles/largeDecor'),
            'stone': bulkImageLoad('tiles/stone'),
            'player': loadImage('entities/character-idle.png')  # import all images needed for the level to be rendered
        }
        
        self.player = physicsEntity(self, 'player', (50, 50), (8, 15))
        
        self.tilemap = tilemap(self)
    
    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            
            self.tilemap.render(self.screen)
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # if loops to detect and use keyboard input to control movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
