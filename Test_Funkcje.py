import Funkcje

def test_add():
    assert Funkcje.add(7, 3) == 10
    assert Funkcje.add(7, -1) == 6
    assert Funkcje.add (4.3, 5.5) == 9.8

test_add()


def test_product():
    assert Funkcje.product(2, 4) == 8
    assert Funkcje.product(3, 1) == 3
    assert Funkcje.product(4, 2) == 8

test_product()

def test_kwadrat():
    assert Funkcje.kwadrat(4) == 16
    assert Funkcje.kwadrat(3) == 9
    assert Funkcje.kwadrat(2) == 4

test_kwadrat()


