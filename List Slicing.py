marks = [99, 88, 77, 66, 55, 44, 33, 22, 11]
print(marks[0:8]) # This will print element from index 1 to 8 (9 is not included)
print(marks[1:]) # aagar hum starting index de rhy h or ending index nahi de rhy h to ye last tak ke element ko lega 

print(marks[-2:-7]) #agar hum negative index use krta h to ye last se lekr -2 index se lekr -7 tak ke element ko lega

#List Slicing
# list slicing is a powerful feature in python that allows you to access a portion of a list by specifying a star index and end index.
#mtlb ki list slicing ka use krke hum list ke kisi bhi part ko access kr sakte h 
# list slicing ka syntax h [start:end:step]
# start se lekar end tak ke elements ko access krta h 
# step ka use krke hum list ke elements ko skip kr sakte h

#list_name[starting_idx:ending_idx]  note:- ending index is not included in the output
# list_name[starting_idx:ending_idx:step]  note:- step is optional and default value is 1
# list_name[starting_idx:]  note:- ending index is not specified, it will take all elements from starting index to end of the list
# list_name[:ending_idx]  note:- starting index is not specified, it will take all elements from start of the list to ending index
# list_name[:]  note:- it will take all elements from start to end of the list