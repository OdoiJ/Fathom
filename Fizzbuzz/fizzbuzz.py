list1 = [0,1,2,3,4,11,12,17]
list2 = [5,6,7,13,33,19,16]
def fizzbuzz(list1,list2):
    total_length = len(list1) + len(list2)
    if total_length % 5 == 0 and total_length % 3 == 0:
        return ("fizzbuzz")   
    if total_length % 3 == 0:
        return ("Fizz")
    if total_length % 5 == 0:
        return ("Buzz")
    # if total_length % 5 == 0 and total_length % 3 == 0:
    #     return ("fizzbuzz")   
    else:
        return(total_length) 

print(fizzbuzz(list1,list2))        
       