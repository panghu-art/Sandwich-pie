def oj(x,y):
    if y==0:
        return x
    else:
        return oj(y,x%y)
print(oj(4,2))
