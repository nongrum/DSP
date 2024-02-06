def count_occurrences_using_count(lst, element):
    
    occurrences = lst.count(element)
    return occurrences

# Example Usage:
my_list = [1, 2, 3, 4, 2, 2, 5]

element_to_count = 2

result = count_occurrences_using_count(my_list, element_to_count)

print(f"Occurrences of {element_to_count} in the list: {result}")
