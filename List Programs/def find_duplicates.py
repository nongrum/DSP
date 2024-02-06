def find_duplicates(lst):
    
    seen = set()
    duplicates = set(x for x in lst if x in seen or seen.add(x))
    return list(duplicates)

# Example Usage:
my_list = [1, 2, 3, 4, 2, 5, 6, 3]

result = find_duplicates(my_list)

print("Original List:", my_list)
print("Duplicates in the list:", result)
