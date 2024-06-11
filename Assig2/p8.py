

def outer():
    massege = " I am the Outer Function "

    def inner():
        return massege
    return inner


if __name__=="__main__":
    inner_function = outer()
    result = inner_function()
    print(result)
