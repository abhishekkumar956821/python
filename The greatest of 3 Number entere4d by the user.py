#WAP to find rhe greatest of 3 numbers entered by the user.

num = int(input("Enter the first number: "))

num1 = int(input("Enter the second number: "))

num2 = int(input("Enter the third number: "))

if(num >= num1 and num >= num2):
    print("The greatest number is ", num)
elif(num1 >= num and num1 >= num2):
    print("The greatest number is ", num1)
elif(num2 >= num and num2 >= num1):
    print("The greatest number is ", num2)
else:
    print("All numbers are equal")  
    