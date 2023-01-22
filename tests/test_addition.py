from pyapp.main  import addition, subtraction


def test_addition():
    assert addition(4, 5) == 9
    assert addition(4, -5) == -1
    assert addition(-4, 5) == 1
    assert addition(-4, -5) == -9
    assert addition(0, -5) == -5
    assert addition(-4, 0) == -4
    assert addition(0, 0) == 0


def test_subtration():
    assert subtraction(1, 2) == -1
    assert subtraction(2, 1) == 1
    assert subtraction(9, 9) == 0
    assert subtraction(-5, 2) == -7
    assert subtraction(-5, -2) == -3
    assert subtraction(0, 0) == 0
    assert subtraction(7, 2) == 5
    assert subtraction(5, 2) > 0

    





