def add(x, y):
    return x+y

def test_add():
    assert add(7, 3) == 10
    assert add(7, -1) == 6
    assert add (4.3, 5.5) == 9.8

test_add()


def product(x, y):
    return x * y

def test_product():
    assert product(2, 4) == 8
    assert product(3, 1) == 3
    assert product(2, 4) == 8

test_product()