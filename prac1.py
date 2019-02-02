# base_no = int(input("enter base:"))
# pow_no = int(input("enter power:"))
def power(base_no, pow_no):
    result = 1
    for index in range (pow_no):
        result = result*base_no
    return result

print(power(3, 4))     
