def age1(x=5,y=10,z=2):#x是有几个人，y是第一个人的岁数，z是每个人比上个人大几岁
    age=0
    if x > 1:
        age=age1(x-1,y,z)+z
        return age
    else:
        return age+y
b=age1()
print('第五个人%d岁'%b)
    
