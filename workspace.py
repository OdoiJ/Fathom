list1 = [2,0,6,5,1,7,'z','a']
def arrange(list1):
    even_nos = '206'
    odd_nos = '517'
    chars = 'za'
    for x in list1:
        if x in even_nos:
            dict1 = {'evens':'2,0,6'}
            return (dict1)
print(arrange(list1))