# "The print() function shows the value as it is,"
# " and the input() function always returns the value as a string. "
# "So, when we check the type, it will give 'str' as the answer."


input("Enter your name :")

age = input("Enter your age :")
print("you entered :", age )


# "The print() function shows the value as it is, "
# "and the input() function always returns the value as a string."
# " So, when we check the type, "
# "it will give 'str' as the answer."



val = input("Enter some value :")
print(type(val),val)




# If we want to take an integer value as input,
#  we need to use type casting like int(input()).
# This way, the value we receive will be in integer format.


val = int(input("Enter your age :"))
print(type(val),val)