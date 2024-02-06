def rotate_array(arr, k):
   
    n = len(arr)
    k = k % n  


    rotated_array = arr[-k:] + arr[:-k]

    return rotated_array

my_array = [1, 2, 3, 4, 5]
rotation_count = 2

result = rotate_array(my_array, rotation_count)

print(f"Original Array: {my_array}")
print(f"Rotated Array: {result}")
