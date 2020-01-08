c=input("请输入文件名：")
f=open(c,'w')
print("请输入内容【单独输入':w'保存退出：】")
while 1:
    y=input()
    if y != ':w':
       f.write('%s\n'%y)
    else:
       break
f.close()

