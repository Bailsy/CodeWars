def tower_builder(floorn):
    tower = []
    for i in range(1, floorn+1):
       tower.append(" "*int(((2*(floorn)-1)-(2*(i)-1))/2)+"*"*int(2*(i)-1)+" "*int(((2*(floorn)-1)-(2*(i)-1))/2))
    return tower
print(tower_builder(3))