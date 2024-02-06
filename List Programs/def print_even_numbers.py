def print_even_numbers(lst):
 

    even_numbers = [num for num in lst if num % 2 == 0]
    
    if even_numbers:
        print("Even numbers in the list:", even_numbers)
    else:
        print("There are no even numbers in the list.")

# Example Usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print_even_numbers(my_list)
