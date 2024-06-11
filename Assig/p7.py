


def outer():

    def inner(a,b):
        print(a+b)

    inner(10,20)
    return inner

m=outer()
v=m(5,5)
print(m)
print(id(v))




