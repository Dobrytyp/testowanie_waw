class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_color(self, color):
        self.color = color

car = Car("BMW", "czarny")

car.change_color("Czerwony")

print(car.color)