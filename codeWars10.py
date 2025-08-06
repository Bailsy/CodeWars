def likes(names):
    c = 0
    for n in names:
        c = c + 1 
        
    if(c == 0):
        return "no one likes this"
    elif(c == 1):
        return names[0] + " likes this"
    elif(c == 2):
        return names[0] + " and " + names[1] + " like this"
    elif(c == 3):
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(c-2) + " others like this"
    
#remember len will go through items in a list and count them
#so there's absolutely no need to iterate through them in a for loopo
print(likes(["Max", "John", "Mark"]))   