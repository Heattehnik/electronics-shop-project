from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, sim_count):
        self.sim_count = sim_count
        super().__init__(name, price, quantity)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
