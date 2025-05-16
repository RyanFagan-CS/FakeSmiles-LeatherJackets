#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
