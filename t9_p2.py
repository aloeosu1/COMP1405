def palindrome(word):
    #getting rid of spaces
    word = word.replace(" ","")
    #if length of word is 0 or 1
    if len(word) == 0 or len(word) == 1:
        return True
    #if first letter doesn't equal last letter
    elif word[0]!=word[-1]:
        return False
    #recursive case
    else:
        return palindrome(word[1:-1])