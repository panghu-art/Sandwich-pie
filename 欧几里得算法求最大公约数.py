def gcd(x,y):
    yue=1
    while yue != 0:
       yue=x%y
       x,y=y,yue
    else:
       return x
print(gcd(12,6))
       
    
