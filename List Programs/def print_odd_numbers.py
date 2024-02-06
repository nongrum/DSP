def print_odd_numbers(lst):
    
    odd_numbers = [num for num in lst if num % 2 != 0]
    
    if odd_numbers:
        print("Odd numbers in the list:", odd_numbers)
    else:
        print("There are no odd numbers in the list.")

# Example Usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print_odd_numbers(my_list)
