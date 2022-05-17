

word=input("ugee oruulna uu  :")
print("original str is ",word)
size=len(word)


print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])