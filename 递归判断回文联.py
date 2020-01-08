def sinz(x):
    b=False
    if (x[0]==x[-1])and(len(x)>1):
        y=x[1:-1]
        b=sinz(y) and True
        return b
    else:
        return False if len(x)>1 else True
if sinz('上海自来水来自海上'):
    print('是回文联')
else:
    print('不是回文联')
       
        

    
