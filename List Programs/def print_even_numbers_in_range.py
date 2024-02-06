def print_even_numbers_in_range(start, end):
   
    even_numbers = [num for num in range(start, end) if num % 2 == 0]

    if even_numbers:
        print("Even numbers in the range:", even_numbers)
    else:
        print("There are no even numbers in the specified range.")

# Example Usage:
start_range = 1
end_range = 10

print_even_numbers_in_range(start_range, end_range)
