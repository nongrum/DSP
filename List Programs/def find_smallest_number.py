def find_smallest_number(lst):
   
    if not lst:
        return None  

    smallest = lst[0]  

    for element in lst[1:]:
        if element < smallest:
            smallest = element

    return smallest


my_list = [5, 2, 8, 1, 4]

result = find_smallest_number(my_list)

if result is not None:
    print(f"Smallest number in the list: {result}")
else:
    print("The list is empty.")
