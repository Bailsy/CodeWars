def score(dice):
    
    sum = 0
    if(dice.count(5)==1):
        sum+=50
    if(dice.count(1)==1):
        sum += 100      
    if(dice.count(1)==3):
        sum += 100       
    if(dice.count(2)==3):
        sum+= 200
    if(dice.count(3)==3):
        sum+= 300
    if(dice.count(4)==3):
        sum+=400
    if(dice.count(5)==3):
        sum+=500
    if(dice.count(6)==3):
        sum+=600
    return sum
print(score([5, 1, 3, 4, 1]))       



    

