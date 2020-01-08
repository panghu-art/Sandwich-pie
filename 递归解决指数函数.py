def power(x,y):
    if y==2:
        return x*x
    else:
        return power(x,y-1)*x
print(power(4,3))
    
