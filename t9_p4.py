def squareList(lis):
    #base case
    if len(lis)==0:
        return lis
    elif len(lis)==1:
        return [lis[0]**2]
    else:
        return [lis[0]**2] + squareList(lis[1:])