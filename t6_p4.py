def palindrome(s):
    #making blank list for reversing string
    sReverse = []
    #removing spaces in string
    s = s.replace(" ","")
    #converting string into list (can compare after)
    s=list(s)
    #testing
    print(s)
    #looping for each index in the list
    for i in range(len(s)):
        #adding each element to reverse list in reverse order
        sReverse.insert(0, s[i])
        
    #if the reverse list has the same data as original string (palindrome)
    if s == sReverse:
        return "True"
    else:
        return "False"


s = "hello world"
print(palindrome(s))
