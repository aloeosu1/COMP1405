def count(string, token):
    if len(string)==0:
        return 0
    #if letter equals token
    elif string[0]==token:
        return 1 + count(string[1:],token)
    #if letter doesn't equal token
    else:
        return 0 + count(string[1:],token)