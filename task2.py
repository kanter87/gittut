print("Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number. ")

previous_num = 0 

for i in range(1,11):
    x_sum =previous_num+i
    print("Current number ",i,"previus num",previous_num,"sum",x_sum)
    previous_num=i 