#creating function
def remove(s, tok):
    #replaces all tokens in the string with a blank
    s = s.replace(tok, "")
    #prints final string
    print(s)

remove("This is as it is","is")