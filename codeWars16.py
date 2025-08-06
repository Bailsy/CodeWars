
def sum_dig_pow(a, b):
    eureka = []
    
    for i in range(a, b+1):
        power = 0
        sum = 0
        for n in str(i):
            power += 1
            sum += pow(int(n), power)
        if sum == i:
            eureka.append(i)
    return eureka    

print(sum_dig_pow(89, 135))