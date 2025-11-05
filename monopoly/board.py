from monopoly.data import tiles_data

class Board:

    def __init__(self):
        self.tiles = tiles_data

    def get_location_info(self, location):
        return self.tiles[location]