"""
Most words in Pig Latin end in "ay." Use the rules below to translate normal English into Pig Latin.

1. If a word starts with a consonant and a vowel, put the first letter of the word at the end of the
word and add "ay."

Example: Happy = appyh + ay = appyhay

2. If a word starts with two consonants move the two consonants to the end of the word and
add "ay."

Example: Child = IIdch + ay = Ildchay

3. If a word starts with a vowel add the word "way" at the end of the word.
Example: Awesome = Awesome +way = Awesomeway

"""
def isVowel(char):
    vowels = ['a','e','i','o','u']
    if char in vowels:
        return True
    else:
        return False

def pigLatinTranslate(word):
    if isVowel(word[0]) != True and isVowel(word[1]):
        print(word[1:] + word[:1])


pigLatinTranslate('famous')