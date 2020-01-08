def findstr(str1,str2):
    '''这是一个寻找字符串中子字符串出现次数的函数'''
    k=0
    if len(str2) != 2:
        print('不好意思，第二个参数长度必须为2，请重新调用！')
    else:
        for b in range(len(str1)):
            if str1[b]==str2[0]:
                if str1[b+1]==str2[1]:
                    k += 1
    return k
print(findstr('fashljkfhasjkfhasjkldfhashfasdhfjklhasjklf','as'))
                       
                   
                   
