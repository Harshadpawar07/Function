

def count(x):
    List = [1,2,3,3,4,5,3]
    count = 0
    for i in List :
        if(x==i):
            count+=1
    return count

    
N = int(input(" : "))
obj = count(N)
print(obj)


