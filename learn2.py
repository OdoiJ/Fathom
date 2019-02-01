# def sayhi(name, age):
#     print("Hello "  + name + ", you are " + age)
# sayhi("Leo", "17")    
l = input("enter a word: ")
def getvowels(l):
    vowels = "aeiou"
    vowel = ""
    for x in l:
       if x in vowels:
           vowel += str(l)
    noduplicates = set(vowel)
    duplicates = len(vowel)-len(noduplicates)
    return (noduplicates,duplicates)
print(getvowels(l))







