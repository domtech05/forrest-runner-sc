import pygame

neighborOffsets = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
physicsTiles = {'grass', 'stone'}


class tilemap:
    def __init__(self, game, tileSize=16):
        self.game = game
        self.tileSize = tileSize
        self.tilemap = {}
        self.offgridTiles = []
        
        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
    
    def tilesAround(self, pos):
        tiles = []
        tileLocation = (int(pos[0] // self.tileSize), int(pos[1] // self.tileSize))
        for offset in neighborOffsets:
            checkLocation = str(tileLocation[0] + offset[0]) + ';' + str(tileLocation[1] + offset[1])
            if checkLocation in self.tilemap:
                tiles.append(self.tilemap[checkLocation])
        return tiles
    
    def physicsRectsAround(self, pos):
        rects = []
        for tile in self.tilesAround(pos):
            if tile['type'] in physicsTiles:
                rects.append(
                    pygame.Rect(tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize, self.tileSize,
                                self.tileSize))
        return rects
    
    def render(self, screen, offset=(0,0)):
        for tile in self.offgridTiles:
            screen.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'] - offset[0], tile['pos'] - offset[1])
        
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            screen.blit(self.game.assets[tile['type']][tile['variant']],
                      (tile['pos'][0] * self.tileSize - offset[0], tile['pos'][1] * self.tileSize - offset[1]))