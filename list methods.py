# Part 1: Reversing a List
my_list = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", my_list)
my_list.reverse()  # Reversing the list
print("Reversed List:", my_list)

# Part 2: Sorting a list of strings
fruits = ["date", "apple", "cherry", "apricot"]
print("\nOriginal List of Strings:", fruits)
fruits.sort()  # Sorting in ascending order
print("Sorted (Ascending) Strings:", fruits)
fruits.sort(reverse=True)  # Sorting in descending order
print("Sorted (Descending) Strings:", fruits)

# Part 3: Demonstrating various list methods
my_list = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nNew List:", my_list)

my_list.append(11)  # Adding 11 at the end
my_list.insert(0, 0)  # Adding 0 at the beginning
print("After append and insert:", my_list)

my_list.remove(5)  # Removing first occurrence of 5
print("After removing 5:", my_list)

my_list.pop()  # Removing last element
print("After popping last element:", my_list)

my_list.sort()  # Sorting in ascending order
print("After sorting (ascending):", my_list)

my_list.reverse()  # Reversing the list
print("After reversing:", my_list)

# Let's demonstrate index, count, copy, extend
index_of_4 = my_list.index(4)  # Finding index of 4
count_of_4 = my_list.count(4)  # Count of 4
print("Index of 4:", index_of_4)
print("Count of 4:", count_of_4)

copied_list = my_list.copy()  # Copying the list
print("Copied list:", copied_list)

my_list.extend([12, 13, 14])  # Extending with another list
print("After extending:", my_list)

# Clear the list
my_list.clear()
print("After clearing:", my_list)
