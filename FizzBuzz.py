


from re import S


def fizzybuzzy():
    i = 2
    s = ""
    for i in range(100):
        if(i % 3 ==0 and i % 5 ==0):
            s = "FizzBuzz!"
        elif(i % 5 == 0):
            s = "Buzz"
        elif(i % 3 == 0):
            s = "Fizz"
        else:
           s = i 
        print(s)

                     
fizzybuzzy()
