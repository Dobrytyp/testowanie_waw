from Klasy import Car

def test_Car_init():
    car = Car("BMV", "Red")
    assert car.name == "BMV"

def test_Car_change_color():
    car = Car("BMV", "Red")
    car.change_color("black")
    assert car.color == "black"