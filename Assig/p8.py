

def outer():
    def inner():
        return "Hello"
    return inner()

retobj=outer()
retinner = retobj
print(retinner)
