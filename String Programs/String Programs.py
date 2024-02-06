#Python program to check if a string is palindrome or not:

def is_palindrome(s):
    return s == s[::-1]

# Example usage:
string_to_check = "radar"
if is_palindrome(string_to_check):
    print("1. The string is a palindrome.")
else:
    print("1. The string is not a palindrome.")

#Python program to check whether the string is Symmetrical or Palindrome:
def is_symmetrical(s):
    return s == s[::-1]

# Example usage:
string_to_check = "radar"
if is_symmetrical(string_to_check):
    print("2. The string is symmetrical.")
else:
    print("2. The string is not symmetrical.")

#Reverse words in a given String in Python:
def reverse_words(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

# Example usage:
input_string = "Hello World"
result = reverse_words(input_string)
print("3. Original String:", input_string)
print("   Reversed String:", result)

#Ways to remove i’th character from a string in Python:

def remove_ith_character(s, i):
    return s[:i] + s[i+1:]

# Example usage:
original_string = "example"
index_to_remove = 2
result = remove_ith_character(original_string, index_to_remove)
print("4. Original String:", original_string)
print("   String after removing character at index", index_to_remove, ":", result)

#Python | Check if a Substring is Present in a Given String:

def is_substring_present(s, substring):
    return substring in s

# Example usage:
main_string = "Hello, World!"
substring_to_check = "World"
if is_substring_present(main_string, substring_to_check):
    print(f"5. {substring_to_check} is present in the string.")
else:
    print(f"5. {substring_to_check} is not present in the string.")

#Python – Words Frequency in String Shorthands:
    
from collections import Counter

def word_frequency(s):
    return dict(Counter(s.split()))

# Example usage:
input_string = "This is a sample string. This string is just a sample."
result = word_frequency(input_string)
print("6. Word frequency:", result)

#Python – Convert Snake case to Pascal case:

def snake_to_pascal(s):
    words = s.split('_')
    pascal_case = ''.join(word.capitalize() for word in words)
    return pascal_case

# Example usage:
snake_case_string = "python_programming"
result = snake_to_pascal(snake_case_string)
print("7. Snake Case String:", snake_case_string)
print("   Pascal Case String:", result)

#Find length of a string in Python (4 ways):

# Method 1: Using len() function
string = "Hello, World!"
length_method_1 = len(string)

# Method 2: Using a loop
length_method_2 = 0
for char in string:
    length_method_2 += 1

# Method 3: Using list comprehension
length_method_3 = sum(1 for char in string)

# Method 4: Using the count() method
length_method_4 = string.count('')

print(f"8. Method 1: {length_method_1}")
print(f"   Method 2: {length_method_2}")
print(f"   Method 3: {length_method_3}")
print(f"   Method 4: {length_method_4}")

#Python program to print even length words in a string:

def even_length_words(s):
    words = s.split()
    even_length_words_list = [word for word in words if len(word) % 2 == 0]
    return even_length_words_list

# Example usage:
input_string = "This is a sample string with some words."
result = even_length_words(input_string)
print("9. Even Length Words:", result)

#Python program to accept the strings which contain all vowels:

def contains_all_vowels(s):
    vowels = set("aeiou")
    return set(s.lower()) >= vowels

# Example usage:
input_string = "education"
if contains_all_vowels(input_string):
    print("10. The string contains all vowels.")
else:
    print("    The string does not contain all vowels.")

#Python | Count the Number of matching characters in a pair of strings:
    
def count_matching_characters(str1, str2):
    common_characters = set(str1) & set(str2)
    return len(common_characters)

# Example usage:
string1 = "hello"
string2 = "world"
result = count_matching_characters(string1, string2)
print("11. Number of Matching Characters:", result)

#Remove all duplicates from a given string in Python:

def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

# Example usage:
input_string = "programming"
result = remove_duplicates(input_string)
print("12. Original String:", input_string)
print("    String after removing duplicates:", result)

#Python – Least Frequent Character in String:

from collections import Counter

def least_frequent_character(s):
    char_count = Counter(s)
    return min(char_count, key=char_count.get)

# Example usage:
input_string = "programming"
result = least_frequent_character(input_string)
print("13. Least frequent character:", result)

#Python | Maximum frequency character in String:

from collections import Counter

def most_frequent_character(s):
    char_count = Counter(s)
    return max(char_count, key=char_count.get)

# Example usage:
input_string = "programming"
result = most_frequent_character(input_string)
print("14. Most frequent character:", result)

#Python | Program to check if a string contains any special character:

import string

def contains_special_character(s):
    return any(char in string.punctuation for char in s)

# Example usage:
input_string = "Hello, World!"
if contains_special_character(input_string):
    print("15. The string contains special characters.")
else:
    print("    The string does not contain special characters.")

#Python | Program to check if a string contains any special character:

import string

def contains_special_character(s):
    return any(char in string.punctuation for char in s)

# Example usage:
input_string = "Hello, World!"
if contains_special_character(input_string):
    print("15. The string contains special characters.")
else:
    print("    The string does not contain special characters.")

#Generating random strings until a given string is generated:
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_until_match(target_string):
    generated_string = ""
    while generated_string != target_string:
        generated_string = generate_random_string(len(target_string))
        print(generated_string)

# Example usage:
target_string = "example"
print("16. Generating random strings until a given string is generated:")
generate_until_match(target_string)

#Find words which are greater than given length k:

def words_greater_than_length(s, k):
    words = s.split()
    return [word for word in words if len(word) > k]

# Example usage:
input_string = "This is a sample string with some long words."
k_value = 4
result = words_greater_than_length(input_string, k_value)
print(f"17. Words greater than {k_value} characters:", result)

#Python program for removing i-th character from a string:

def remove_ith_character(s, i):
    return s[:i] + s[i+1:]

# Example usage:
original_string = "example"
index_to_remove = 2
result = remove_ith_character(original_string, index_to_remove)
print("18. Original String:", original_string)
print("    String after removing character at index", index_to_remove, ":", result)

#Python program to split and join a string:

def split_and_join(s):
    words = s.split()
    joined_string = '-'.join(words)
    return joined_string

# Example usage:
input_string = "This is a sample string"
result = split_and_join(input_string)
print("19. Original String:", input_string)
print("    String after split and join:", result)

#Python | Check if a given string is a binary string or not:

def is_binary_string(s):
    return all(bit in '01' for bit in s)

# Example usage:
binary_string = "110101"
if is_binary_string(binary_string):
    print("20. The string is a binary string.")
else:
    print("    The string is not a binary string.")

#Python program to find uncommon words from two Strings:

def uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    uncommon_words_list = list(words1.symmetric_difference(words2))
    return uncommon_words_list

# Example usage:
string1 = "Hello World"
string2 = "World of Python"
result = uncommon_words(string1, string2)
print("21. Uncommon words:", result)

#Python – Replace duplicate Occurrence in String:

def replace_duplicate_occurrence(s):
    char_count = {}
    result = ''
    for char in s:
        if char in char_count:
            char_count[char] += 1
            result += str(char_count[char])
        else:
            char_count[char] = 1
            result += char
    return result

# Example usage:
input_string = "programming"
result = replace_duplicate_occurrence(input_string)
print("22. Original String:", input_string)
print("    String after replacing duplicate occurrences:", result)

#Python – Replace multiple words with K:

def replace_multiple_words(s, words, k):
    for word in words:
        s = s.replace(word, k)
    return s

# Example usage:
input_string = "Python is an amazing programming language. Python is versatile."
words_to_replace = ["Python", "language"]
k_value = "Java"
result = replace_multiple_words(input_string, words_to_replace, k_value)
print("23. Original String:", input_string)
print("    String after replacing multiple words with K:", result)

#Python | Permutation of a given string using inbuilt function:

from itertools import permutations

def string_permutations(s):
    return [''.join(perm) for perm in permutations(s)]

# Example usage:
input_string = "abc"
result = string_permutations(input_string)
print("24. Permutations of the string:", result)

#Python | Check for URL in a String:

import re

def contains_url(s):
    pattern = re.compile(r'https?://\S+')
    return bool(pattern.search(s))

# Example usage:
input_string = "Visit our website at https://www.example.com for more information."
if contains_url(input_string):
    print("25. The string contains a URL.")
else:
    print("    The string does not contain a URL.")

#Execute a String of Code in Python:

def execute_code(code_string):
    try:
        exec(code_string)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
code_to_execute = "print('Hello, World!')"
print("26. Executing code:")
execute_code(code_to_execute)

#String slicing in Python to rotate a string:

def rotate_string(s, k):
    rotated_string = s[k:] + s[:k]
    return rotated_string

# Example usage:
input_string = "abcdef"
rotation_count = 2
result = rotate_string(input_string, rotation_count)
print("27. Original String:", input_string)
print("    String after rotating:", result)

#String slicing in Python to check if a string can become empty by recursive deletion:

def is_empty_by_deletion(s):
    while '[]' in s or '{}' in s or '()' in s:
        s = s.replace('[]', '').replace('{}', '').replace('()', '')
    return not s

# Example usage:
input_string = "{[()]}{}"
if is_empty_by_deletion(input_string):
    print("28. The string can become empty by recursive deletion.")
else:
    print("    The string cannot become empty by recursive deletion.")

#Python Counter | Find all duplicate characters in a string:
    
from collections import Counter

def find_duplicate_characters(s):
    char_count = Counter(s)
    duplicates = [char for char, count in char_count.items() if count > 1]
    return duplicates

# Example usage:
input_string = "programming"
result = find_duplicate_characters(input_string)
print("29. Duplicate characters:", result)

#Python – Replace all occurrences of a substring in a string:

def replace_substring(s, old, new):
    return s.replace(old, new)

# Example usage:
input_string = "Hello, World!"
old_substring = "World"
new_substring = "Python"
result = replace_substring(input_string, old_substring, new_substring)
print("30. Original String:", input_string)
print("    String after replacing all occurrences of a substring:", result)



    

