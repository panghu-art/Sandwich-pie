def sumj(*param,base=3):
    '''这是一个计算参数与基数积的函数'''
    for sum1 in param:
        sum1 += sum1
    if base == 3:
        sum1 *= 3
    elif base == 5:
        sum1 *= 5
    else:
        print('您输入的基数base错误，请将base基数设置为3或者5！')
        return(None)
    return sum1
print(sumj(1,2,3,base=5))
