
m = input("enter a word:")
def countVowel(m):
    vowels = 'AEIOUaeiou'
    vowel = ""
    counter = 0
    for x in m:
        if x in vowels:
            if x in vowel:
                counter += 1
            else:
                vowel += str(x)

    
    return (vowel, counter)

       
  
       
print(countVowel(m))