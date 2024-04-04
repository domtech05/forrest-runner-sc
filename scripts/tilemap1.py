class tilemap:  # create class for tilemaps
    def __init__(self, game, tileSize=16):  # initialise class and all variables needed within class
        self.game = game
        self.tileSize = tileSize
        self.tilemap = {}
        self.offgridTiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(i + 5)] = {'type': 'stone', 'variant': 1, 'pos': (10, i + 5)}  # set tilemap types and positions

    def render(self, screen):
        for tile in self.offgridTiles:
            screen.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])  # render the offgrid tiles

        for location in self.tilemap:
            tile = self.tilemap[location]
            screen.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize))
            # render the on grid tiles
