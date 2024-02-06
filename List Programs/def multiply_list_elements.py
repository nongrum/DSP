def multiply_list_elements(lst):
   
    result = 1
    for element in lst:
        result *= element
    return result

# Example Usage:
my_list = [1, 2, 3, 4, 5]

result = multiply_list_elements(my_list)

print(f"List: {my_list}")
print(f"Product of elements in the list: {result}")
