def find_largest_element(arr):
    if not arr:
        return None  

    largest = arr[0]  

    for element in arr[1:]:
        if element > largest:
            largest = element

    return largest

my_array = [10, 5, 8, 20, 15]
result = find_largest_element(my_array)

if result is not None:
    print(f"The largest element in the array is: {result}")
else:
    print("The array is empty.")
