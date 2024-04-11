import pygame

neighborOffsets = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]  # offsets to get 9 tiles surrounding and including current tile
physicsTiles = {'grass', 'stone'}


class tilemap:  # create class for tilemaps
    def __init__(self, game, tileSize=16):  # initialise class and all variables needed within class
        self.game = game
        self.tileSize = tileSize
        self.tilemap = {}
        self.offgridTiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(i + 5)] = {'type': 'stone', 'variant': 1, 'pos': (10, i + 5)}  # set tilemap types and positions

    def tilesAround(self, pos):
        tiles = []  # tiles to return from function

        tileLocation = (int(pos[0] // self.tileSize), int(pos[1] // self.tileSize))  # Convert pixel position to grid position

        for offset in neighborOffsets:  # Generate the 9 tiles around position given above
            checkLocation = str(tileLocation[0] + offset[0]) + ';' + str(tileLocation[1] + offset[1])  # location to check
            if checkLocation in self.tilemap:  # check there is a tile in given location
                tiles.append(self.tilemap[checkLocation])
        return tiles


    def physicsRectsAround (self, pos):  # Filter nearby tiles for only those that have physics enabled
        rects = []  # tiles to return
        for tile in self.tilesAround(pos):  # check all tiles within set radius from character as set using above function
            if tile['type'] in physicsTiles:  # check given tiles against physicsTiles dictionary
                rects.append(pygame.Rect(tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize, self.tileSize, self.tileSize))
                # create rects from all physics-enabled tiles
        return rects


    def render(self, screen):
        for tile in self.offgridTiles:
            screen.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])  # render the offgrid tiles


        for location in self.tilemap:
            tile = self.tilemap[location]
            screen.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize))
            # render the on grid tiles
