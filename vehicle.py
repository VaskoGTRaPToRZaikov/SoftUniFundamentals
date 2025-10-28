class Vehicle:

    def __init__(self, type: str, model: str, price: int):
        self.price = price
        self.model = model
        self.type = type
        self.owner = None

    def buy(self, money: int, owner: str):
        if money < self.price:
            return "Sorry, not enough money"

        if self.owner is not None:
            return "Car already sold"

        change = money - self.price
        self.owner = owner
        return f"Successfully bought a {self.type}. Change: {change:.2f}"

    def sell(self):
        if self.owner is not None:
            self.owner = None
            return self.owner
        return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"
