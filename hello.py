def myCal(num1, num2):
    product =num1 * num2
    if product <= 1000:
        return product 
    else :
        return num1+num2
    
    result = myCal(20,30)
    print("the result is", result)
