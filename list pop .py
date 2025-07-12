#list.pop(index)
# This method removes and returns the element at the specified index from the list
#mtlb ki ye method list se specified index ka element ko remove kr deta h aur us element ko return bhi kr deta h

list1 = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List1:", list1)
removed_element = list1.pop(4) # Removing the element at index 4
print("List after popping element at index 4:", list1)
print("Removed Element:", removed_element) # This will print the removed element, which is 5 in this case