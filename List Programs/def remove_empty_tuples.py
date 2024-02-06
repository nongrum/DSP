def remove_empty_tuples(lst):
    
    updated_list = [tup for tup in lst if tup]
    return updated_list

# Example Usage:
my_list = [(1, 2), (), (3, 4), (), (5, 6)]

result = remove_empty_tuples(my_list)

print("Original List of Tuples:", my_list)
print("List after removing empty tuples:", result)
