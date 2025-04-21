import math
sideA = int(input("what is the first length of the triangle?"))
sideB = int(input("what is the second length of the triangle?"))
sideC = int(input("what is the third length of the triangle?"))
semiS = 0.5 * (sideA+sideB+sideC)
area = math.sqrt((semiS * (semiS-sideA) * (semiS-sideB) * (semiS-sideC)))
print (area)
