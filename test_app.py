from app import soma, multiplica

def test_multiplica():
    assert multiplica(2, 3) == 6
    assert multiplica(-1, 5) == -5
    assert multiplica(0, 10) == 0