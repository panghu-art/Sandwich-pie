begin=1
dictp={}
while begin:
   print('|————欢迎进入通讯录程序————|')
   print('|————1：查询联系人资料 ————|')
   print('|————2: 插入新的联系人 ————|')
   print('|————3：删除已有联系人 ————|')
   print('|————4：退出通讯录程序 ————|')
   order=int(input("请输入相关指令代码："))
   if order == 1:
       name=input("请输入联系人姓名：")
       if name in dictp:
           print('%s的电话是：%s'%(name,dictp[name]))
       else:
           print('抱歉，没有这个联系人的信息')         
   elif order == 2:
       name=input("请输入联系人姓名：")
       if name in dictp:
           print('您输入的姓名在通讯录中已存在——》%s:%s'%(name,dictp(name)))
           i=input('是否要修改用户资料（Y//N）:')
           if i == "Y":
              tel=input("请输入用户联系电话：")
              dictp[name]=tel
       else:
            tel=input("请输入用户联系电话：")
            dictp[name]=tel
   elif order == 3:
       name=input('输入您要删除的联系人姓名：')
       del dictp[name]
   elif order == 4:
       print('|————感谢使用通讯录程序————|')
       begin=0
   else:
       print("指令输入错误，没有这个指令！")
