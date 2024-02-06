def print_positive_numbers_in_range(start, end):
  
    positive_numbers = [num for num in range(start, end) if num > 0]

    if positive_numbers:
        print("Positive numbers in the range:", positive_numbers)
    else:
        print("There are no positive numbers in the specified range.")

# Example Usage:
start_range = -5
end_range = 5

print_positive_numbers_in_range(start_range, end_range)
