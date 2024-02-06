def cumulative_sum(lst):
   
    result = [sum(lst[:i+1]) for i in range(len(lst))]
    return result

# Example Usage:
my_list = [1, 2, 3, 4, 5]

result = cumulative_sum(my_list)

print("Original List:", my_list)
print("Cumulative sum of the list:", result)
