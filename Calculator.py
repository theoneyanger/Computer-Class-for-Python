def add(a, b):
    return int(a) + int(b)
def sub(a, b):
    return int(a) - int(b)
def mult(a, b):
    return int(a) * int(b)
def div(a, b):
    if b == 0: # handle ZeroDivision error
        return 'Error'
    return int(a) / int(b)