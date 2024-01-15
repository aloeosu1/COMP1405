def pow(b, x):
    #if exponent(x) == 0
    if x == 0:
        return 1
    #recursive case
    else:
        return b * pow(b, x-1)