def shu(*num):
    for i in range(len(num)):
        alpha=0
        dig=0
        space=0
        other=0
        for x in range(len(num[i])):
            c=num[i][x]
            if c.isalpha():
                alpha += 1
            elif c.isdigit():
                dig += 1
            elif c.isspace():
                space +=1
            else:
                other +=1
        print('第%d个参数中含%d个字母、%d个数字、%d个空格、%d个其他字符。'%(i+1,alpha,dig,space,other))
shu('zhangasdsdfj shadjkadjkj dsjafjdfiaifi +_+(9-0f89aahda','ahfdjkajsfkaskl;dfjal;s  uuuu2389u324123490','asdfjkjsdajsadf 12378123787364664++___+')
