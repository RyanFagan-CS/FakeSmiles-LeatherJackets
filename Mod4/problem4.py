#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.

gRated = 13
pg13Rated = 17

userAge = int(input("what is your age? "))
 
if userAge > pg13Rated:
    print("You can see R Rated Films.")
elif userAge < gRated:
    print("You can see G Rated Films.")
elif userAge >= gRated:
    print("You can see PG-13 Rated Films.")
