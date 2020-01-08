def siny(n):
    result=[]
    if n:
        result=siny(n//10)
        result.append(n%10)
        return result
    else:
        return result
print(siny(1000))
    
