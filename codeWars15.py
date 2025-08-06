def controller(events):
    eventDialog = ""
    P = False
    C = 0
    O = False
    
    Closed = True
    Opening = False
    for i in events:
        
        if C == 0:
            Closed = True
            Opening = False
        elif C == 5:
            Closed = False
            Opening = False 
        else:
            Opening = True
            

            
        if i == "." and P == False and Closed == True:
            eventDialog += "0"    
            
        if i == "P":
            P = True
            
        if P == True and Closed == True:
            C += 1
            eventDialog += str(C)
            





            
    return eventDialog
print(controller("P...."))