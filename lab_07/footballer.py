class Footballer:
    def __init__(self, name, country, pos, price) -> None:
        self.name = name
        self.country = country
        self.pos = pos
        self.price = float(price)

    def __str__(self):
        return f'{self.price}, {self.name}, {self.country}, {self.pos}'