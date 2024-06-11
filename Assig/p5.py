
def sumNum(x):
    sum = 1
    for i in range(1,x+1):
        sum *= i
    print(sum)

num = int(input("enter value for num : ")) 
sumNum(num)
