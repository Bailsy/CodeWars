
def divisors(integer):
    for i in range(1, integer):
        if integer % i == 0:
            print(i)


divisors(12)