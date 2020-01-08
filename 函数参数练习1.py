def sum(*param,base=3):
    s=0
    if base == 5:
        for i in param:
            s = s + i
    else:
        base=3
        for i in param:
            s = s + i
        s=base*s
    return s
print(sum(1,1,1,4,base=3))
