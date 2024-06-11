

def mult(List):
    Num = 1
    N = list()
    for i in List:
        Num = Num*i
        N.append(Num)
    return N


obj = mult([1,2,3,4,5])
print(obj)

