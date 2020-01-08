num=list(input('请输入一串数字：'))
print(num)
sum=0
for i in range(len(num)):
    print(range(len(num)))
    if type(num[i])==type(1):
        sum=sum+num[i]
        print(sum)
print(sum)
