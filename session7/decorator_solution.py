from functools import wraps

def smart_divide(func):
    """ ana el wa7sh"""
    @wraps(func)
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    "enta meen"
    print(a/b)


divide(4,2) 
divide(4,0)   