def find_n_largest_elements(lst, n):
   
    if len(lst) < n:
        return None  # Return None if the list has fewer than N elements

    # Sort the list in descending order and take the first N elements
    largest_elements = sorted(lst, reverse=True)[:n]

    return largest_elements

# Example Usage:
my_list = [5, 2, 8, 1, 4]
n = 3

result = find_n_largest_elements(my_list, n)

if result is not None:
    print(f"{n} largest elements in the list: {result}")
else:
    print("The list has fewer than N elements.")
