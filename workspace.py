list1 = [2,0,6,5,1,7,'a']
def arrange(w):
    even_nos = []
    odd_nos = []
    chars = []
    for x in w:
        if isinstance(x, str):
            chars.append(x)
            chars.sort()
            # print("character")
        elif isinstance(x, int):
            if x%2 ==0 :
                even_nos.append(x) 
                even_nos.sort()
                # print("is even")
            elif x%2 ==1:
                odd_nos.append(x)
                odd_nos.sort()
                # print("is odd")
    return {'evens':even_nos ,'odds':odd_nos, 'chars':chars}       

# mydict['evens'] = sorted(even_nos)
# mydict['odds'] = sorted(odd_nos)
# mydict['chars'] = sorted(chars)

            
print(arrange(list1))