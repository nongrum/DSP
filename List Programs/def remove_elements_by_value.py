def remove_elements_by_value(lst, values_to_remove):
    
    updated_list = [element for element in lst if element not in values_to_remove]
    return updated_list

# Example Usage:
my_list = [1, 2, 3, 4, 5, 6, 7]
elements_to_remove = [2, 4, 6]

result = remove_elements_by_value(my_list, elements_to_remove)

print("Original List:", my_list)
print("List after removing elements:", result)
