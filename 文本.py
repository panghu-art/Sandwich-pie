def change(filename,old,new):
    txt=[]
    num=0
    f=open(filename,'r')
    for each in f:
        if old in each:
            num1=each.count(old)
            txt1=each.replace(old,new)
            txt.append(txt1)
            num += num1
    #for i in range(len(txt)):
    print(txt)
    fw=open(filename,'w')
    fw.writelines(txt)
    fw.close()
    f.close()
    print(num)
file=input('请输入文件名：')
old=input('请输入需要替换的单词或字符：')
new=input('请输入新的单词或字符：')
change(file,old,new)

    
            
    
