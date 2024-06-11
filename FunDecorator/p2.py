
def normalfun(**args):
    sum = 0
    for k,v in args.items():
        sum+=v
    return sum
    

ret = normalfun(x=20,y=30)
print(ret)
