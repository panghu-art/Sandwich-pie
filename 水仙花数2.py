def find():
    b=[]
    for i in range(100,1000):
        k=i
        j=''
        x=i%10
        i=i//10
        y=i%10
        i=i//10
        z=i%10
        if (x**3+y**3+z**3)==k:
            j=str(z)+str(y)+str(x)
            b.append(j)
    return b
print(find())
        
                 
