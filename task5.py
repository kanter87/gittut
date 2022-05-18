print("Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.")


def  MatchNumbers(numbers):
    print("given list",numbers)
    FirstNumber=numbers[0]
    LastNumber=numbers[-1]

    if FirstNumber==LastNumber:
        return True
    else:
        return False

    

    
numbers_x = [10, 20, 30, 40, 10]    
print(MatchNumbers(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print(MatchNumbers(numbers_y))
