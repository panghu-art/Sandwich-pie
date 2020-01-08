begin=1
use={}
while begin:
    print("|————新建用户：N/n————|")
    print("|————登陆账号：E/e————|")
    print("|————退出程序：Q/q————|")
    order=input("请输入指令代码：")
    if (order == "N")or(order == "n"):
        name=input("请输入用户名：")
        while name in use:
            name=input("此用户名已经被使用,请重新输入：")
        else:
            use[name]=input("请输入密码：")
        print(use)
    elif(order == "E")or(order == "e"):
        name=input("请输入用户名：")
        while name in use:
            ecode=input("请输入密码：")
            while ecode == use[name]:
                print("欢迎进入系统！")
                break
            else:
                print("密码输入错误!")
                continue
            break
        else:
            print("用户名不存在,请重新输入：",end='')
            name=input()
            continue               
    elif(order == "Q")or(order == "q"):
        print("欢迎使用系统，下次再见！")
        break
    else:
        print("指令输入错误！")
        
    

