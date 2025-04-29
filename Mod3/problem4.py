#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
data = input("What data would you like me to search? ")
idx1 = int(input("Where can I find the start of the information you want? "))
idx2 = int(input("Where can I find the end of the information you want? "))
print (data[idx1:idx2])