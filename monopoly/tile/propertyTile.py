from monopoly.tile.tile import Tile


class PropertTile(Tile):

    def __init__(self, name, type, price, rent, city):
        super().__init__(name, type)
        self.price = price
        self.rent = rent
        self.city = city