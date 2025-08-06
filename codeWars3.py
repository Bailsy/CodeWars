
import string


def create_phone_number(n):   
    n = list(map(str, n))    
    return str('('+n[0]+n[1]+n[2]+')'+' '+n[3]+n[4]+n[5]+'-'+n[6]+n[7]+n[8]+n[0])

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))