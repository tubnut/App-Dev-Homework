def isVowel(char):
    vowels = ['a','e','i','o','u']
    if char in vowels:
        return True
    else:
        return False

def toPigLatin(word):
    word = word.lower()
    if isVowel(word[0]) != True and isVowel(word[1]) == True:
        return word[1:] + word[:1] + "ay"
    elif isVowel(word[0]) == False and isVowel(word[1]) == False:
        return word[2:] + word[:2] + "ay"
    elif isVowel(word[0]) == True:
        return word + "ay"


print(toPigLatin('famous'))
print(toPigLatin('gluten'))
print(toPigLatin('happy'))
print(toPigLatin('alphabet'))
print(toPigLatin('child'))
print(toPigLatin('crusty'))