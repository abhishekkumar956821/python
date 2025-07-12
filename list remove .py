#list.remove method ka mtlb h list se kisi element ko remove krna
#list.remove(value) # This method removes the first occurrence of a specified value from the list
#agar haam list.remove(value) use krte h to ye list se specified value ko remove kr deta h      

list = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]          
print("Original List:", list)
list.remove(3) # Removing the first occurrence of 3 from the list
print("List after removing 3:", list)


#list.pop(index) # This method removes and returns the element at the specified index from the list
list1 = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List1:", list1)
removed_element = list1.pop(4) # Removing the element at index 4
print("List after popping element at index 4:", list1)
print("Removed Element:", removed_element) # This will print the removed element, which is 5 in this case