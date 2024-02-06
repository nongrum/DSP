def find_remainder(arr, n):
   
    result = 1

   
    for element in arr:
        result = (result * element) % n

    return result


my_array = [1, 2, 3, 4, 5]
divisor = 10

remainder = find_remainder(my_array, divisor)

print(f"Original Array: {my_array}")
print(f"Remainder of array multiplication divided by {divisor}: {remainder}")
