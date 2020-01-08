for i in range(100,999):
    x=i%10
    y=((i%100)-x)/10
    z=((i%1000)-x-(y*10))/100
    if i==((x**3)+(y**3)+(z**3)):
        print(i,end=' ')
        
