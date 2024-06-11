

class cricket :

    def __init__(self,capton,Wkeeper,overT20,overtest):
        self.capton = capton
        self.Wkeeper = Wkeeper
        self.overT20 = overT20
        self.overtest = overtest

    def T20(self):
        print(self.capton)
        print(self.Wkeeper)
        print(self.overT20)

    def test(self):
        print(self.capton)
        print(self.Wkeeper)
        print(self.overtest)
        
class child(cricket):

    pass

obj = child("Virat","KL",20,50)
obj.T20()
obj.test()

