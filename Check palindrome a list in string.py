#WAP to check if a list contains a palindrome of element.(Hint: use copy() method)

list1 = ["n","i","t","i","n",]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("NOT Palindrome")