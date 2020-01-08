def sinx(x):
    '''这是一个用递归实现除二取余实现进制转化的函数'''
    b=''
    if x:
        b=sinx(x//2)
        return b+str(x%2)
    else:
        return b
print(sinx(7))
    
