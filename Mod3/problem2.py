#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("what is your name? ")
age = int(input("How old are you? "))
ageNextYear = age + 1
ageNextYear = str(ageNextYear) 
age = str(age) 
print("Hello, " + name + " You are " + age + " years old. Next year, you will be " + ageNextYear + " years old.") 