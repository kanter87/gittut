print("Write a program to remove characters from a string starting from zero up to n and return a new string.")
 
def remove_chars( word ,number ):
    
    print("word is",word )
    x=word[number:]
    return x
print(remove_chars("pynative", 4))
