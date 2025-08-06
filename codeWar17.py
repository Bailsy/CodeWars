def solution(number):
    listy = []
    for i in range(0, number):
        if((i%3)==0 or (i%5)==0):
            listy.append(i)
            
    return sum(listy)

print(solution(10))