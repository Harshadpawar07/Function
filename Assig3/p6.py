

class Parent :
    print("In class")

    def __del__(self):
        print("In Dis")

obj1 = Parent()
obj2 = Parent()
obj3 = Parent()
obj4 = Parent()
obj3 = obj1
del(obj2)
