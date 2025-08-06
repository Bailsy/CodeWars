

def generate_hashtag(s):
    s=s.title()
    cCount = 0
    for c in s:
        cCount = cCount + 1
        if c == " ":
           s=s.replace(c,'')
           
    if(cCount > 140 or cCount == 0):
        return False
    else:
      return "#"+s   
    
    
print(generate_hashtag("hello"))
