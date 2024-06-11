


def Gen():
    print("In Genrator")
    yield 10
    yield 20
    yield 30
    yield 40
    print("End fun")
    yield Gen()

obj = Gen()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


