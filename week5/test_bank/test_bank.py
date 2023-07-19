import bank


def test_value_hello():
    assert bank.value("hello, world") == 0
    assert bank.value("Hello") == 0
    assert bank.value("HELLO") == 0


def test_value_h():
    assert bank.value("hi") == 20
    assert bank.value("Hey") == 20
    assert bank.value("HOLA") == 20


def test_value_other():
    assert bank.value("welcome") == 100
    assert bank.value("Good morning") == 100
    assert bank.value("12345") == 100


def test_value_empty_string():
    assert bank.value("") == 100


if __name__ == "__main__":
    test_value_hello()
    test_value_h()
    test_value_other()
    test_value_empty_string()
    print("All tests passed!")
