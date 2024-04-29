import pygame
import json


AUTOTILE_MAP = {
    tuple(sorted([(1, 0), (0, 1)])): 0,
    tuple(sorted([(1, 0), (0, 1), (-1, 0)])): 1,
    tuple(sorted([(-1, 0), (0, 1)])): 2,
    tuple(sorted([(-1, 0), (0, -1), (0, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1)])): 4,
    tuple(sorted([(-1, 0), (0, -1), (1, 0)])): 5,
    tuple(sorted([(1, 0), (0, -1)])): 6,
    tuple(sorted([(1, 0), (0, -1), (0, 1)])): 7,
    tuple(sorted([(1, 0), (-1, 0), (0, 1), (0, -1)])): 8,
}
neighborOffsets = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]  # offsets for tiles around player
physicsTiles = {'grass', 'stone'} #  tiles that have physics applied to them
AUTOTILE_TYPES = {'grass', 'stone'}


class tilemap:
    def __init__(self, game, tileSize=16):
        #  define all parameters for tilemap
        self.game = game
        self.tileSize = tileSize
        self.tilemap = {}
        self.offgridTiles = []
        
    
    def tilesAround(self, pos): #  find the tiles located around the player
        tiles = []
        tileLocation = (int(pos[0] // self.tileSize), int(pos[1] // self.tileSize))
        for offset in neighborOffsets:
            checkLocation = str(tileLocation[0] + offset[0]) + ';' + str(tileLocation[1] + offset[1])
            if checkLocation in self.tilemap:
                tiles.append(self.tilemap[checkLocation])
        return tiles
    
    def save(self, path):
        f = open(path, 'w')
        json.dump({'tilemap': self.tilemap, 'tileSize': self.tileSize, 'offgrid': self.offgridTiles}, f)
        f.close()
    
    def load(self, path):
        f = open(path, 'r')
        mapData = json.load(f)
        f.close()
        
        self.tilemap = mapData['tilemap']
        self.tileSize = mapData['tile_size']
        self.offgridTiles = mapData['offgrid']
        
        
    
    def physicsRectsAround(self, pos): #  Apply physics to the applicable tiles around the player
        rects = []
        for tile in self.tilesAround(pos):
            if tile['type'] in physicsTiles:
                rects.append(
                    pygame.Rect(tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize, self.tileSize,
                                self.tileSize))
        return rects
    
    def autotile(self):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            neighbors = set()
            for shift in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                check_loc = str(tile['pos'][0] + shift[0]) + ';' + str(tile['pos'][1] + shift[1])
                if check_loc in self.tilemap:
                    if self.tilemap[check_loc]['type'] == tile['type']:
                        neighbors.add(shift)
            neighbors = tuple(sorted(neighbors))
            if (tile['type'] in AUTOTILE_TYPES) and (neighbors in AUTOTILE_MAP):
                tile['variant'] = AUTOTILE_MAP[neighbors]
                
    
    def render(self, screen, offset=(0,0)):
        for tile in self.offgridTiles:
            screen.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'] - offset[0], tile['pos'] - offset[1])
        
        for x in range(offset[0] // self.tileSize, (offset[0] + screen.get_width()) // self.tileSize + 1): #  find the coordinates of the left and right sides of the display
            for y in range(offset[1] // self.tileSize, (offset[1] + screen.get_height()) // self.tileSize + 1):  # find the coordinates of the top and bottom sides of the display
                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    screen.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tileSize - offset[0], tile['pos'][1] * self.tileSize - offset[1]))
