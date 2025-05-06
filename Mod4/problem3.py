#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.
threshold = 100
balance = 0

balance = int(input("What is your total bank balance? "))

if balance > threshold:
    print("False")
else:
    print("True")