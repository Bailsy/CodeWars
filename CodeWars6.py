def get_sum(a, b):
    n = 0 
    if(a<b):
        n1 = a
        n2 = b+1
    elif(a>b):
        n1 = b
        n2 = a+1
    else:
        return b
 
    for i in range(n1, n2):   
        n = i + n 
    return n

print(get_sum(0,-1))