

class Parent :

    @classmethod
    def fun(self):
        print("In fun")

    @staticmethod
    def gun():
        print("In gun")

    def run(self):
        print("In run")

class child(Parent):
    pass

obj = child()
obj.fun()
obj.gun()
obj.run()
