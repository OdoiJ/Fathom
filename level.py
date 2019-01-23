x = int(input("year of birth"))
age = 2019 - x
print(age)
if age  <= 18:
    print("you are a minor")
elif age < 36:
    print("you are a youth")
else:
    print("you are an elder")
