def print_odd_numbers_in_range(start, end):
    
    odd_numbers = [num for num in range(start, end) if num % 2 != 0]

    if odd_numbers:
        print("Odd numbers in the range:", odd_numbers)
    else:
        print("There are no odd numbers in the specified range.")

# Example Usage:
start_range = 1
end_range = 10

print_odd_numbers_in_range(start_range, end_range)
