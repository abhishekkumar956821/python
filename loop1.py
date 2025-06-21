name = "Abhishek kumar"
friend = "Deepanshu"
anotherfriend = 'lavi'
apple = ''' he said
hi Abhishek 
hey i am good
i want to eat an apple'''
print("hello," + name)
print(apple)
# In python , String is like an array of characters.
#  we can access parts of string by using its index which start from 0.
#Square brackets can be used to access element of the string.


print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])

# LOOPING THROUGH THE STRING
# We can loop through strings using a foor loop like this 
# for characters in name:
#       print(characters)

print("lets use a for loop\n")

for character in name:
    print(character)


print("lets use a for loop\n") 

for character in apple:
    print(character)