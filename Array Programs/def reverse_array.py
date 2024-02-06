def reverse_array(arr, start, end):
    """
    Helper function to reverse elements in the array from index 'start' to 'end'.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(arr, k):
   
    
    n = len(arr)
    k = k % n  

    
    reverse_array(arr, 0, n - k - 1)

    reverse_array(arr, n - k, n - 1)

    reverse_array(arr, 0, n - 1)

my_array = [1, 2, 3, 4, 5]
rotation_count = 2

rotate_array_reversal(my_array, rotation_count)

print(f"Original Array: {my_array}")
