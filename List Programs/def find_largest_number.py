def find_largest_number(lst):
    
    if not lst:
        return None 

    largest = lst[0]  

    for element in lst[1:]:
        if element > largest:
            largest = element

    return largest

my_list = [5, 2, 8, 1, 4]

result = find_largest_number(my_list)

if result is not None:
    print(f"Largest number in the list: {result}")
else:
    print("The list is empty.")
