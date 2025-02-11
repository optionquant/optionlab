x:int
x = 1000.25
print(x)

def sayHello(x:int):
    print("hello", x)
    return x
    
def test_dummy():
    result = sayHello(100.25)
    assert type(result) == float
    

#if __name__ == '__main__':
#    sayHello(100.25)