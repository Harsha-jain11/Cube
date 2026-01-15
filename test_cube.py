from cube import cube_of_number


def test_positive_number():
    assert cube_of_number(3) == 27


def test_negative_number():
    assert cube_of_number(-2) == -8


def test_zero():
    assert cube_of_number(0) == 0
