#nesting statement ka mtlb hota h ek condition ke under dusri condition ko likhna prper space ke sath 
#like
# if condition1:
#     if (condition2):
#         if condition1:
#             print("Hello")
# Example of nesting statement

marks = int(input("Enter your marks: ") )

if(marks >= 90):
    if(marks >= 95):
        print("Excellent! Grade A+")
    else:
        print("Grade A")
elif(marks >= 80):
    if(marks >= 85):
        print("Good job! Grade B+") 
    else:
        print("Grade B")
elif(marks >= 70):
    if(marks >= 75):        
        print("Well done! Grade C+")        
    else:
        print("Grade C")
elif(marks >= 60):
    if(marks >= 65):
        print("Keep it up! Grade D+")   
    else:
        print("Grade D")    
else:
    print("fail")