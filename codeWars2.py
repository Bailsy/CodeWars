
def shortcut( s ):
    for c in 'aioue':
        s = s.replace(c, '')   
    return(s)    

print(shortcut("hello"))