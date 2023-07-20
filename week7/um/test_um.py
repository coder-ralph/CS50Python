from um import count

def main():
    test_1()
    test_2()
    test_3()
    
def test_1():
    assert count("um") == 1
    
def test_2():
    assert count("um, um. yummy") == 2
    
def test_3():
    assert count("Um. thanks for the album.") == 1
    assert count("hello, world") == 0
    
if __name__ == "__main__":
    main()