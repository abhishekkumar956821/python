#This code checks if a user is eligible to vote based on their age.
#if the age is 18 or elder, it prints "You are eligible to vote".
#else, it prints "You are not eligible to vote".

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

