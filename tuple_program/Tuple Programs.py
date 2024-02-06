#Python program to Find the size of a Tuple:
def tuple_size(input_tuple):
    return len(input_tuple)

# Example usage:
sample_tuple = (1, 2, 3, 4, 5)
result = tuple_size(sample_tuple)
print("1. Size of the tuple:", result)

#Python – Maximum and Minimum K elements in Tuple:

def max_min_k_elements(input_tuple, k):
    sorted_tuple = sorted(input_tuple)
    max_k_elements = sorted_tuple[-k:]
    min_k_elements = sorted_tuple[:k]
    return max_k_elements, min_k_elements

# Example usage:
sample_tuple = (4, 2, 8, 1, 6)
k_value = 2
result_max, result_min = max_min_k_elements(sample_tuple, k_value)
print("2. Maximum", k_value, "elements in the tuple:", result_max)
print("   Minimum", k_value, "elements in the tuple:", result_min)

#Create a list of tuples from the given list having the number and its cube in each tuple:

def create_tuples_list(input_list):
    tuples_list = [(num, num**3) for num in input_list]
    return tuples_list

# Example usage:
numbers_list = [1, 2, 3, 4]
result = create_tuples_list(numbers_list)
print("3. List of tuples with number and its cube:", result)

#Python – Adding Tuple to List and vice – versa:

def add_tuple_to_list(tuples_list, new_tuple):
    tuples_list.append(new_tuple)
    return tuples_list

def add_list_to_tuple(input_tuple, new_list):
    result_tuple = input_tuple + tuple(new_list)
    return result_tuple

# Example usage:
original_list = [(1, 2), (3, 4), (5, 6)]
new_tuple = (7, 8)
result_list_add = add_tuple_to_list(original_list, new_tuple)
print("4. List after adding tuple:", result_list_add)

original_tuple = (1, 2, 3)
new_list = [4, 5, 6]
result_tuple_add = add_list_to_tuple(original_tuple, new_list)
print("   Tuple after adding list:", result_tuple_add)

#Python – Closest Pair to Kth index element in Tuple:

def closest_pair_to_kth_element(tuples_list, k):
    kth_element = tuples_list[k]
    closest_pair = min(tuples_list, key=lambda x: abs(x[0] - kth_element[0]) + abs(x[1] - kth_element[1]))
    return closest_pair

# Example usage:
tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
k_index = 2
result = closest_pair_to_kth_element(tuple_list, k_index)
print("5. Closest pair to the", k_index, "index element:", result)

#Python – Join Tuples if similar initial element:

def join_tuples_with_similar_initial(tuples_list):
    result_list = []
    temp_dict = {}
    for tuple_item in tuples_list:
        initial_element = tuple_item[0]
        if initial_element in temp_dict:
            temp_dict[initial_element] += tuple_item[1:]
        else:
            temp_dict[initial_element] = tuple_item
    for value in temp_dict.values():
        result_list.append(tuple(value))
    return result_list

# Example usage:
tuple_list = [(1, 2), (1, 3), (2, 4), (3, 5), (2, 6)]
result = join_tuples_with_similar_initial(tuple_list)
print("6. List of tuples after joining similar initial elements:", result)

#Python – Extract digits from Tuple list:

def extract_digits(tuples_list):
    digit_list = [int(str(num)[1]) for tup in tuples_list for num in tup if str(num)[0] == '-']
    return digit_list

# Example usage:
tuple_list = [(-12, 34), (-45, 67), (89, -10)]
result = extract_digits(tuple_list)
print("7. List of digits extracted from tuple list:", result)

#Python – All pair combinations of 2 tuples:

def all_pair_combinations(tuple1, tuple2):
    result_combinations = [(x, y) for x in tuple1 for y in tuple2]
    return result_combinations

# Example usage:
tuple1 = (1, 2)
tuple2 = ('a', 'b')
result = all_pair_combinations(tuple1, tuple2)
print("8. All pair combinations of 2 tuples:", result)

#Python – Remove Tuples of Length K:

def remove_tuples_of_length_k(tuples_list, k):
    result_list = [tup for tup in tuples_list if len(tup) != k]
    return result_list

# Example usage:
tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8, 9)]
k_value = 2
result = remove_tuples_of_length_k(tuple_list, k_value)
print("9. List of tuples after removing tuples of length", k_value, ":", result)

#Sort a list of tuples by the second Item:

def sort_list_of_tuples_by_second_item(tuples_list):
    result_list = sorted(tuples_list, key=lambda x: x[1])
    return result_list

# Example usage:
tuple_list = [(3, 4), (1, 2), (5, 6), (2, 8)]
result = sort_list_of_tuples_by_second_item(tuple_list)
print("10. List of tuples sorted by the second item:", result)

#Python program to Order Tuples using an external List:

def order_tuples_using_external_list(tuples_list, order_list):
    result_list = sorted(tuples_list, key=lambda x: order_list.index(x[0]))
    return result_list

# Example usage:
tuple_list = [('apple', 2), ('banana', 1), ('orange', 3)]
order_list = ['banana', 'apple', 'orange']
result = order_tuples_using_external_list(tuple_list, order_list)
print("11. List of tuples ordered using external list:", result)

#Python – Flatten tuple of List to tuple:

def flatten_tuple_of_lists(input_tuple):
    result_tuple = tuple(item for sublist in input_tuple for item in sublist)
    return result_tuple

# Example usage:
nested_tuple = ([1, 2], [3, 4], [5, 6])
result = flatten_tuple_of_lists(nested_tuple)
print("12. Tuple after flattening tuple of lists:", result)

#Python – Convert Nested Tuple to Custom Key Dictionary:

def convert_nested_tuple_to_dict(nested_tuple):
    result_dict = {tup[0]: tup[1] for tup in nested_tuple}
    return result_dict

# Example usage:
nested_tuple = (('a', 1), ('b', 2), ('c', 3))
result = convert_nested_tuple_to_dict(nested_tuple)
print("13. Dictionary converted from nested tuple:", result)
