print('这是一个验证密码的程序：')
number='zhangrui'
password=''
password=input('请输入密码：')
i=1
while i<3:
   if '*'in password:
      print('密码不能包含*字符，请重新输入：',end=' ')
      password=input()
      continue
   if number != password:
      i += 1
      print('密码输入错误！请重新输入：',end=' ')
      password=input()
   else: 
      i += 1
      print('密码输入正确!')
      break
if i >3:
    print('输入次数太多，密码锁定！')

        
