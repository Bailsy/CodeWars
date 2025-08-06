
#use two for loops

def get_sum(n):
    res = []
    for i in range(n+1, 0, -1):
        for n in range(1, i+1):
            i = i + 2
            res.append(i-2)
    return sum(res)
print(get_sum(20000))