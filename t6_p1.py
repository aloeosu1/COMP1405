def product(L):
    #setting product to 1
    product = 1
    #looping for length of list
    for i in range (len(L)):
        #mutliplying product by each element in list
        product = L[i]*product
    #returns product
    return product

product = product([3,2,5,2])
print(product)

