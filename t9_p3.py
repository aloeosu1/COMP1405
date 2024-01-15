def filterVowels(string):
    #defining vowels
    vowels = "aeiou"
    #if empty string
    if string == "":
        return string
    #if first letter is a vowel
    elif string[0] in vowels:
        #do nothing with first letter
        return filterVowels(string[1:])
    #if first letter is not a vowel
    else:
        #return the first letter + the function with first letter removed
        return string[0]+filterVowels(string[1:])