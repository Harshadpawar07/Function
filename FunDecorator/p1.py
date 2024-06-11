

def decorfun(func):
    
    def wrapper():
        print("In Wrapper")
        func()
        print("In Wrapper")

    return wrapper

def normalfun():
    print("In NoramlFun")

normalfun = decorfun(normalfun)
normalfun()
