

def parent():
    def digitcount(x):
        count = 0
        for i in x:
            count+=1
        print(count)
        return count
    return digitcount("12345")
    
    def evendigitcount(x):
        count = 0
        for i in x:
            if(x[i]%2==0):
                count+=1
            return count
    return evendigitcount("12345")

obj = parent()
print(obj)
