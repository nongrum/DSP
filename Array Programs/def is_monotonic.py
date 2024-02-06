def is_monotonic(arr):
  
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False


    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

monotonic_array = [1, 2, 3, 4, 5]
non_monotonic_array = [1, 2, 3, 2, 4]

result_monotonic = is_monotonic(monotonic_array)
result_non_monotonic = is_monotonic(non_monotonic_array)

print(f"Is the array {monotonic_array} monotonic? {result_monotonic}")
print(f"Is the array {non_monotonic_array} monotonic? {result_non_monotonic}")
