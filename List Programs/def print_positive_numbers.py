def print_positive_numbers(lst):
    
    positive_numbers = [num for num in lst if num > 0]

    if positive_numbers:
        print("Positive numbers in the list:", positive_numbers)
    else:
        print("There are no positive numbers in the list.")

# Example Usage:
my_list = [-3, -1, 0, 2, 4, -5, 6]

print_positive_numbers(my_list)
