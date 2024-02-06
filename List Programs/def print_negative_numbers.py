def print_negative_numbers(lst):
   
    negative_numbers = [num for num in lst if num < 0]

    if negative_numbers:
        print("Negative numbers in the list:", negative_numbers)
    else:
        print("There are no negative numbers in the list.")

# Example Usage:
my_list = [-3, -1, 0, 2, 4, -5, 6]

print_negative_numbers(my_list)
