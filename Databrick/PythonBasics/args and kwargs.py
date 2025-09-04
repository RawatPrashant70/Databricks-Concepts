# *args and **kwargs
# In Python functions, *args and **kwargs allow passing a variable number of arguments to a function

def example(*args, **kwargs):
    print(type(args), type(kwargs)) # args -> tuple and kwargs -> dict

    for i in args:
        print(i, end=" ")
    print("\n")

    for key,value in kwargs.items():
        print(key, value)
    print("\n")

if __name__ == "__main__":
    example(3,4,5) # here we have 3 parameters
    example(6,7)   # in this cas we have only 2 parameters
    example(name="RAM", Class="10th")
    example(1,2,3,[4,5],name="RAM", Class="10th")