def remove_empty_lists(lst):
   
    updated_list = [sublist for sublist in lst if sublist]
    return updated_list

# Example Usage:
my_list = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

result = remove_empty_lists(my_list)

print("Original List of Lists:", my_list)
print("List after removing empty lists:", result)
