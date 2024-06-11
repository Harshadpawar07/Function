

def outer():
    def inner():
        return " This is the Inner function "
    return inner

if __name__=="__main__":
    retobj = outer()
    retInner = retobj()

    print(retInner)
