def find_second_largest_number(lst):
   
    if len(lst) < 2:
        return None  # Return None if the list has less than two elements

    largest = second_largest = float('-inf')

    for element in lst:
        if element > largest:
            second_largest = largest
            largest = element
        elif element > second_largest and element != largest:
            second_largest = element

    if second_largest == float('-inf'):
        return None  # There is no second-largest number

    return second_largest

# Example Usage:
my_list = [5, 2, 8, 1, 4]

result = find_second_largest_number(my_list)

if result is not None:
    print(f"Second-largest number in the list: {result}")
else:
    print("The list has less than two elements.")
