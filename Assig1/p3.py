

def outer():
    def inner():
        return " Hello , I am the inner function "
    return inner

retobj = outer()
retinner = retobj()
print(retinner)
