from jar import Jar


def test_init():
    jar = Jar(4)
    assert jar.capacity == 4
    assert jar.size == 0
    jar1 = Jar()
    assert jar1.capacity == 12
    
    
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(4)
    assert jar.size == 8
    jar.deposit(4)
    assert jar.size == 12


    
def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(4)
    assert jar.size == 8
    jar.withdraw(4)
    assert jar.size == 4
    jar.withdraw(4)
    assert jar.size == 0
    

    