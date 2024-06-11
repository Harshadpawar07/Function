

def outer():
    def inner():
        return "Hello, i am inner Function"
    return inner()

ans = outer()
print(ans)
