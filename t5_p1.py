#Michael Han, 101157504, Tutorial 5, problem 1
def pow2(num):
    i = 0
    x=0
    while (x<=num):
        
        x = 2**i
        i+=1    

    if (x>num):
        x = 2**(i-2)
        i-=2
        print(f"2^{i} is {x}")
    else:
        print(f"2^{i} is {x}")
        


       
        
        

            


