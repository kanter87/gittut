

print("Given two integer numbers return their product only if the product is greater than 1000, else return their sum.")

def myCal(num1, num2):
    product =num1 * num2
    if product <= 1000:
        print("this is",product)

    else :
        print(num1+num2)
    
    
myCal(50,60)


#if __name__== '__main__':
 #   myCal()
