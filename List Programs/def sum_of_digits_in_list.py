def sum_of_digits_in_list(lst):
   
    result = [sum(map(int, str(num))) for num in lst]
    return result

# Example Usage:
my_list = [123, 45, 678, 9]

result = sum_of_digits_in_list(my_list)

print("Original List:", my_list)
print("Sum of digits in the list:", result)
