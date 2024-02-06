def print_negative_numbers_in_range(start, end):
   
    negative_numbers = [num for num in range(start, end) if num < 0]

    if negative_numbers:
        print("Negative numbers in the range:", negative_numbers)
    else:
        print("There are no negative numbers in the specified range.")

# Example Usage:
start_range = -5
end_range = 5

print_negative_numbers_in_range(start_range, end_range)
