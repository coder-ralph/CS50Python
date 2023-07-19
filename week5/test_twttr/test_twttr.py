import twttr


def test_shorten():
    assert twttr.shorten("Hello") == "Hll"
    assert twttr.shorten("Python") == "Pythn"
    assert twttr.shorten("elephant") == "lphnt"
    assert twttr.shorten("CS50") == "CS50"
    assert twttr.shorten("AI") == ""
    assert twttr.shorten("") == ""


if __name__ == "__main__":
    test_shorten()
