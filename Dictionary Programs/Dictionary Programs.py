#Python – Extract Unique values dictionary values:
def unique_values(dictionary):
    unique_set = set(val for sublist in dictionary.values() for val in sublist)
    return list(unique_set)

# Example usage:
sample_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
result = unique_values(sample_dict)
print("1. Unique values in dictionary:", result)


#Python program to find the sum of all items in a dictionary:

def sum_of_values(dictionary):
    return sum(sum(values) for values in dictionary.values())

# Example usage:
sample_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
result = sum_of_values(sample_dict)
print("2. Sum of all items in dictionary:", result)

#Python | Ways to remove a key from a dictionary:

def remove_key(dictionary, key_to_remove):
    return {key: value for key, value in dictionary.items() if key != key_to_remove}

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
result = remove_key(sample_dict, key_to_remove)
print(f"3. Dictionary after removing key '{key_to_remove}':", result)

#Ways to sort a list of dictionaries by values in Python – Using itemgetter:

from operator import itemgetter

def sort_list_of_dicts_by_values(list_of_dicts, key):
    return sorted(list_of_dicts, key=itemgetter(key))

# Example usage:
list_of_dicts = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 30}]
key_to_sort_by = 'age'
result = sort_list_of_dicts_by_values(list_of_dicts, key_to_sort_by)
print("4. List of dictionaries sorted by age:", result)

#Ways to sort a list of dictionaries by values in Python – Using lambda function:

def sort_list_of_dicts_by_values_lambda(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])

# Example usage:
list_of_dicts = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 30}]
key_to_sort_by = 'age'
result = sort_list_of_dicts_by_values_lambda(list_of_dicts, key_to_sort_by)
print("5. List of dictionaries sorted by age:", result)

#Python | Merging two Dictionaries:

def merge_two_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result = merge_two_dicts(dict1, dict2)
print("6. Merged Dictionary:", result)

#Python – Convert key-values list to flat dictionary:

def convert_to_flat_dict(keys, values):
    return dict(zip(keys, values))

# Example usage:
keys_list = ['a', 'b', 'c']
values_list = [1, 2, 3]
result = convert_to_flat_dict(keys_list, values_list)
print("7. Flat Dictionary:", result)

#Python – Insertion at the beginning in OrderedDict:

from collections import OrderedDict

def insert_at_beginning(ordered_dict, key_value_pair):
    return OrderedDict([(key_value_pair[0], key_value_pair[1])] + list(ordered_dict.items()))

# Example usage:
ordered_dict = OrderedDict([('a', 1), ('b', 2)])
key_value_pair_to_insert = ('c', 3)
result = insert_at_beginning(ordered_dict, key_value_pair_to_insert)
print("8. OrderedDict after insertion at the beginning:", result)

#Python | Check order of character in string using OrderedDict( ):

from collections import OrderedDict

def check_order(s, pattern):
    char_positions = OrderedDict.fromkeys(pattern)
    index = 0
    for char in s:
        if char in char_positions:
            char_positions[char] = index
            index += 1
    return all(char_positions[char] < char_positions[next_char] for char, next_char in zip(pattern, pattern[1:]))

# Example usage:
input_string = "engineers rock"
pattern_to_check = "egr"
if check_order(input_string, pattern_to_check):
    print("9. Characters are in order in the string.")
else:
    print("    Characters are not in order in the string.")

#Dictionary and counter in Python to find the winner of the election:

from collections import Counter

def election_winner(votes):
    vote_count = Counter(votes)
    max_votes = max(vote_count.values())
    winners = [candidate for candidate, count in vote_count.items() if count == max_votes]
    return min(winners)

# Example usage:
votes_list = ['John', 'Alice', 'Bob', 'Alice', 'Bob', 'John', 'John']
winner = election_winner(votes_list)
print("10. Winner of the election:", winner)

#Python – Append Dictionary Keys and Values (In order) in a dictionary:

def append_keys_values(dictionary):
    result = {}
    for key, value in dictionary.items():
        result[key] = value
        result[value] = key
    return result

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 3}
result = append_keys_values(sample_dict)
print("11. Dictionary after appending keys and values:", result)

#Python | Sort Python Dictionaries by Key or Value:

def sort_dict_by_key_or_value(dictionary, by_key=True):
    return dict(sorted(dictionary.items(), key=lambda x: x[0] if by_key else x[1]))

# Example usage:
sample_dict = {'b': 2, 'a': 1, 'c': 3}
result_key_sort = sort_dict_by_key_or_value(sample_dict, by_key=True)
result_value_sort = sort_dict_by_key_or_value(sample_dict, by_key=False)
print("12. Dictionary sorted by key:", result_key_sort)
print("    Dictionary sorted by value:", result_value_sort)

#Python – Sort Dictionary key and values List:

def sort_dict_keys_values(dictionary):
    sorted_dict = {k: sorted(v) for k, v in dictionary.items()}
    return sorted_dict

# Example usage:
sample_dict = {'b': [2, 1, 3], 'a': [1, 3, 2], 'c': [3, 1, 2]}
result = sort_dict_keys_values(sample_dict)
print("13. Dictionary with sorted keys and values:", result)

#Handling missing keys in Python dictionaries:

from collections import defaultdict

def handle_missing_keys(dictionary, default_value):
    result_dict = defaultdict(lambda: default_value, dictionary)
    return result_dict

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 3}
default_value = 'N/A'
result = handle_missing_keys(sample_dict, default_value)
print("14. Dictionary with default value for missing keys:", result)

#Python dictionary with keys having multiple inputs:

def multi_input_dict(keys, values):
    result_dict = {key: val.split(',') for key, val in zip(keys, values)}
    return result_dict

# Example usage:
keys_list = ['a', 'b', 'c']
values_list = ['1,2,3', '4,5,6', '7,8,9']
result = multi_input_dict(keys_list, values_list)
print("15. Dictionary with keys having multiple inputs:", result)

#Print anagrams together in Python using List and Dictionary:

def print_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    for anagram_group in anagram_dict.values():
        print(anagram_group)

# Example usage:
words_list = ['listen', 'silent', 'enlist', 'hello', 'world']
print("16. Anagrams grouped together:")
print_anagrams(words_list)

#K’th Non-repeating Character in Python using List Comprehension and OrderedDict:

from collections import OrderedDict

def kth_non_repeating_character(s, k):
    char_count = OrderedDict.fromkeys(s, 0)
    for char in s:
        char_count[char] += 1

    non_repeating_chars = [char for char, count in char_count.items() if count == 1]
    if len(non_repeating_chars) >= k:
        return non_repeating_chars[k - 1]
    else:
        return None

# Example usage:
input_string = "geeksforgeeks"
k_value = 3
result = kth_non_repeating_character(input_string, k_value)
print(f"17. {k_value}th non-repeating character:", result)

#Check if binary representations of two numbers are anagram:

def are_binary_anagrams(num1, num2):
    bin_num1 = bin(num1)[2:]
    bin_num2 = bin(num2)[2:]
    return sorted(bin_num1) == sorted(bin_num2)

# Example usage:
number1 = 8
number2 = 4
if are_binary_anagrams(number1, number2):
    print("18. Binary representations are anagrams.")
else:
    print("    Binary representations are not anagrams.")

#Python Counter to find the size of the largest subset of anagram words:

from collections import Counter

def largest_anagram_subset(words):
    word_counter = Counter(''.join(sorted(word)) for word in words)
    return max(word_counter.values())

# Example usage:
words_list = ['cat', 'act', 'dog', 'god', 'tac']
result = largest_anagram_subset(words_list)
print("19. Size of the largest subset of anagram words:", result)

#Python | Remove all duplicates words from a given sentence:

def remove_duplicates(sentence):
    words = sentence.split()
    unique_words = list(set(words))
    return ' '.join(unique_words)

# Example usage:
input_sentence = "Python is great and Python is easy"
result = remove_duplicates(input_sentence)
print("20. Sentence after removing duplicate words:", result)

#Python Dictionary to find mirror characters in a string:

def mirror_characters_dict(s):
    mirror_dict = {'A': 'A', 'M': 'M', 'Y': 'Y', 'T': 'T', 'O': 'O', 'U': 'U', 'I': 'I', 'W': 'W', 'X': 'X', 'V': 'V'}
    result_dict = {char: mirror_dict[char] for char in s if char in mirror_dict}
    return result_dict

# Example usage:
input_string = "MIRROR"
result = mirror_characters_dict(input_string)
print("21. Mirror characters in the string:", result)

#Counting the frequencies in a list using a dictionary in Python:

def count_frequencies(input_list):
    frequency_dict = {}
    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

# Example usage:
input_list = [1, 2, 3, 1, 2, 1, 3, 4, 5]
result = count_frequencies(input_list)
print("22. Frequencies in the list:", result)

#Python | Convert a list of Tuples into a Dictionary:

def list_of_tuples_to_dict(list_of_tuples):
    result_dict = dict(list_of_tuples)
    return result_dict

# Example usage:
tuples_list = [('a', 1), ('b', 2), ('c', 3)]
result = list_of_tuples_to_dict(tuples_list)
print("23. Dictionary converted from list of tuples:", result)

#Python counter and dictionary intersection example (Make a string using deletion and rearrangement):

from collections import Counter

def can_make_string(original_str, target_str):
    original_counter = Counter(original_str)
    target_counter = Counter(target_str)
    return all(original_counter[char] >= target_counter[char] for char in target_str)

# Example usage:
original_string = "xyzabc"
target_string = "axbycz"
if can_make_string(original_string, target_string):
    print("24. The target string can be made from the original string.")
else:
    print("    The target string cannot be made from the original string.")

#Python dictionary, set, and counter to check if frequencies can become the same:

from collections import Counter

def can_frequencies_become_same(s):
    char_count = Counter(s)
    values_set = set(char_count.values())
    return len(values_set) == 1 or (len(values_set) == 2 and 1 in values_set)

# Example usage:
input_string = "xyyz"
if can_frequencies_become_same(input_string):
    print("25. Frequencies can become the same.")
else:
    print("    Frequencies cannot become the same.")

#Scraping And Finding Ordered Words In A Dictionary using Python:

import requests

def ordered_words_from_dictionary(url):
    response = requests.get(url)
    words_list = response.text.split('\n')
    ordered_words = [word for word in words_list if ''.join(sorted(word)) == word]
    return ordered_words

# Example usage:
dictionary_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
result = ordered_words_from_dictionary(dictionary_url)
print("26. Ordered words from the dictionary:", result)

#Possible Words using given characters in Python:

def possible_words(characters, words_list):
    result_words = [word for word in words_list if set(word).issubset(characters)]
    return result_words

# Example usage:
available_characters = {'a', 'b', 'c', 't', 'e', 'r'}
dictionary_words = ['cat', 'bat', 'rate', 'acre', 'art', 'car']
result = possible_words(available_characters, dictionary_words)
print("27. Possible words using given characters:", result)

#Python – Keys associated with Values in Dictionary:

def keys_associated_with_values(dictionary, value_to_find):
    result_keys = [key for key, value in dictionary.items() if value == value_to_find]
    return result_keys

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
value_to_find = 1
result = keys_associated_with_values(sample_dict, value_to_find)
print("28. Keys associated with value", value_to_find, ":", result)


