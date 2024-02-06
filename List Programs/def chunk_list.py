def chunk_list(lst, chunk_size):
    
    result = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    return result

# Example Usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3

result = chunk_list(my_list, chunk_size)

print("Original List:", my_list)
print(f"List after breaking into chunks of size {chunk_size}:", result)
