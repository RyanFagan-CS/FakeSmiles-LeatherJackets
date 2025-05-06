#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off". 
threshold = 8
lightLevel = 0

lightLevel = int(input("how bright is it outside, on a scale of one to ten? "))

if lightLevel > threshold:
    print("Headlights Off")
else:
    print("Headlights On")