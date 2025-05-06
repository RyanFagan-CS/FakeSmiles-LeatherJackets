#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.

threshold = 50
shipping = 5
orderTotal = 0

cartTotal = int(input("What is your order total? "))

if cartTotal < threshold:
    orderTotal = cartTotal + shipping
else:
    orderTotal = cartTotal
print("The total of your order is", orderTotal,"dollars. Have a great day.")