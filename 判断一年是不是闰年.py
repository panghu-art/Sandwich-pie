print('————————这是一个判断是否是闰年的小程序————————')
temp=input("请您输入一个年份：")
year=int(temp)
if (year % 4 == 0)and(year % 100 != 0):
     print("这一年是闰年！")
elif (year % 400 == 0):
    print("这一年是闰年！")
else:
    print('这一年不是闰年！')
    
