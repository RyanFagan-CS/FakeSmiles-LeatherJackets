#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("Enter a positive integer: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("The sum is", sum)
