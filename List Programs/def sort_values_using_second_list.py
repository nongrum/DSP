def sort_values_using_second_list(list1, list2):
    
    combined = list(zip(list2, list1))
    combined.sort()
    result = [element for _, element in combined]
    return result

# Example Usage:
list1 = [1, 2, 3, 4, 5]
list2 = ['b', 'a', 'd', 'c', 'e']

result = sort_values_using_second_list(list1, list2)

print("Original List 1:", list1)
print("Original List 2:", list2)
print("List 1 values sorted using List 2:", result)
