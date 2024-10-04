class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description


class Key(Item):
    def __init__(self):
        super().__init__("Key", "A shiny, golden key.")


class Chest(Item):
    def __init__(self):
        super().__init__("Chest", "A heavy wooden chest.")

class Goldcoins(Item):
    def __init__(self, amount):
        super().__init__("Gold Coins", "A pile of gold coins.")
        self.amount = amount

class Goldencrown(Item):
    def __init__(self):
        super().__init__("Golden Crown", "A majestic crown worn by kings.")