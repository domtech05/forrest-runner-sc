import pygame
from scripts.entities import physicsEntity, player, enemy
from scripts.utils import loadImage, bulkImageLoad
from scripts.tilemap1 import tilemap
from scripts.clouds import clouds


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
            'clouds': bulkImageLoad('clouds')  # import all images needed for the level to be rendered
        }
        
        self.clouds = clouds(self.assets['clouds'], count=35)
        
        self.player = player(self, (50, 50), (8, 15))
        self.enemy = enemy(self, (249, 50), (8, 15))
        
        self.tilemap = tilemap(self)
        self.tilemap.load('map.json')
        
        self.scroll = [0, 0]
    
    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            
            # Setup scrolling variables based on player position
            self.scroll[0] += (self.player.rect().centerx - self.screen.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.screen.get_height() / 2 - self.scroll[1]) / 30
            
            renderScroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            self.clouds.update()
            self.clouds.render(self.screen, offset=renderScroll)

            self.enemy.update(self.tilemap)
            self.enemy.render(self.screen, offset=renderScroll)
            
            # Render tilemap and player, passing in the offset values as calculated above
            self.tilemap.render(self.screen, offset=renderScroll)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen, offset=renderScroll)
            
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
                        self.player.jump()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)