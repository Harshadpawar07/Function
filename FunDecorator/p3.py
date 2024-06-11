
def city(narhe):

    def pPur():
        print("start Pandharpur")
        narhe()
        print("End Pandharpur")

    return pPur

def katraj(narhe):
    print("In Katraj")
    narhe()
    print("In Katraj")

    return katraj

def Pune():
    print("In Pune")

Pune = city(katraj(Pune))
Pune()





