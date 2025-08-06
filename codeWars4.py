def xo(s):
    s = s.lower()
    oNum = 0
    xNum = 0
    for c in s:
        if(c == 'o'):
            oNum = oNum + 1
        if(c == 'x'):
            xNum = xNum + 1
    if(oNum == xNum):
        return True
    else:
        return False
    
print(xo("ooxxx"))