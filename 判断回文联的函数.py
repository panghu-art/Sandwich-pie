def hui():
    '''这是一个判断回文联的函数'''
    x=input('请输入一句话：')
    a=list(x)
    b=a.copy()
    a.reverse()
    num=0
    for i in range(len(a)):
        if a[i] == b[i]:
            num += 1
            continue
        else:
            print('不是回文联！')
            break
    if num == len(a):
        print('是回文联！')
hui()
        
    
    
