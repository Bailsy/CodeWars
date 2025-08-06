def count_bits(n):
    c = 0
    for i in bin(n):
        if i == '1':
            c = c +1
    return c

#remember you could use the count function to count characters in a string

print(count_bits(5))