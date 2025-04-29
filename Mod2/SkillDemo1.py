#WE need 1. Name, 2. Total Bill, 3> People, 4. Total/People 5. 
#Hey (name), each person in your (people)-person party will pay (result)
name = input("what is your name? ")
total = float(input("what is the total bill? "))
partySize = int(input("What is the total number of people in your party? "))
splitBill = (total / partySize)
print("hello", name, "each person in your", partySize,f"person party will need to pay ${splitBill:.2f}")
