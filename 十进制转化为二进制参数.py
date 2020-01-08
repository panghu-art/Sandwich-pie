def bind(num):
    '''这是一个将十进制转化为二进制的函数
    if num in(0,1):
        d=str(num)
    else:
        d=''
        while num not in (0,1):
           d=(str(num%2))+d
           num=num//2
        d=str(num)+d
    return(d)
print(bind(8))'''
    y=1
    z=[]
    b=''
    while y != 0:
        y=num//2
        z.append(num%2)
        num=y
    z.reverse()
    for i in z:
        b=b+str(i)
    return(b)
print(bind(100))

        
