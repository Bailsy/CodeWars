import statistics

def freq_stack(pops, balloons):
    balloons.reverse()
    popped = []
    print(balloons)
    for i in range (0, pops):
        for i in balloons: 
            print(i)      
            if i in statistics.multimode(balloons):
                balloons.remove(i)      
                break
            if statistics.mode(balloons) == []:
                balloons.remove(i)
            print(balloons)
              
            
    return balloons        
        
        
print(freq_stack(3, [1, 1, 2, 3, 4, 5, 6, 7, 8 ]))