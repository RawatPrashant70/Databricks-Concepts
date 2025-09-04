print(" Decorators")
"""

Decorators : A decorator in Python is a function that takes another function as an argument 
and extends or modifies its behavior without changing the original function's code.

Decorators are widely used in real-world Python projects for:
1.Logging and debugging
2.Performance monitoring (timing)
3.Caching results (memoization)
4.Authentication and authorization
5.Rate limiting and retries

"""

# Example-1

def authenticator(func):
    userData = {"Rawat": 6666, "Lakshman": 9999}
    def wrapper(*args, **kwargs):
        _name = kwargs["name"]
        _pin = kwargs["pin"]
        if userData[_name] != _pin:
            print("Not Valid Pin") 
        else:
            return func(*args, **kwargs)
    return wrapper

@authenticator                     #internally->  pin_checker = authenticator(pin_checker)
def pin_checker(name, pin):
    print(f"Welcome... {name}")
    # print(name, pin)

pin_checker(name="Rawat", pin=4524)
pin_checker(name="Lakshman", pin=9999)


# Example -2
# Class decorator

def class_decorator(cls):
    cls.name = "Lakshman"
    return cls

@class_decorator
class basic:
    def __init__(self,_name):
        self.name = _name

obj = basic("Ram")
print(obj.name) # obj is instance -> so it prints instance attribute
print(basic.name) # this is class instance -> so this will print class attribute





"""Generators"""
print("Generators")


"""
A generator in Python is a special type of function that produces 
a sequence of values one at a time ,  instead of computing and storing them 
all at once in memory. 
generators are memory-efficient and useful when working with large sequence
"""

def counting(number):
    start = 1
    while start<=number:
        yield start
        start +=1

value = counting(10)
print(list(value))