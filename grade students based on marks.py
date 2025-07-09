#Grade students Based on marks
#marks >=90 ,grade A
#marks >=80 ,grade B
#marks >=70 ,grade C
#70 > marks ,grade D

marks = int(input("Enter your marks: "))
if(marks >= 90):
    print("Grade A")
elif(marks >= 80):
    print("Grade B")
elif(marks >= 70):
    print("Grade C")
elif(marks >= 60):
    print("Grade D")
elif(marks >= 50):
    print("Grade E")    
elif(marks >= 40):
    print("Grade F")

else:
    print("fail")

# Note: The above code assumes that marks are between 0 and 100.
# If marks can be outside this range, additional checks should be added.
# For example, you might want to handle cases where marks are negative or greater than 100. 