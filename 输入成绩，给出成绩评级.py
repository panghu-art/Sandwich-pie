tri = 1
while tri:
   temp = input("请输入一个成绩：")
   while (not temp.isdigit()):
       print("输入的数据类型错误，必须是整数，请重新输入：",end=' ')
       temp=input()
   score=int(temp)
   if (score >=  90) and (score <= 100):
       print("这个成绩的评级是：A")
       tri = 0
   elif (score >=  80) and (score <90):
       print("这个成绩的评级是：B")
       tri = 0
   elif (score >=  60) and (score < 80):
       print("这个成绩的评级是：C")
       tri = 0
   elif (score >=  0) and (score < 60):
       print("这个成绩的评级是：D")
       tri = 0
   else:
       print("不好意思，您输入的值不在成绩评价范畴，成绩应该在01——100之间！")
print("程序结束，谢谢使用！")
