def get_sum(a, b):
    s=''
    n = 0
    
    if(a == b):
        return (str(b) + " since both are same")

    for i in range(a, b+1):    
        n = i + n 
        if(i<b):
            s = s  + str(i) + '+'
        else:
            s = s + str(i) + '=' + str(n)
        
        
    return s 

print(get_sum(-1, 10))