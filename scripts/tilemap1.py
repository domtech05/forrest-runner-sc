class tilemap:
    def __init__(self, tileSize=16):
        self.tileSize = tileSize
        self.tilemap = {}
        self.offgridTiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(i + 5)] = {'type': 'grass', 'variant': 1, 'pos': (10, i + 5)}
