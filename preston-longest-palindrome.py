long_string = input("Enter a string: ")

long_string_length = len(long_string)
minimum_word_length = 2
longest_palindrome = ""

def reverse_string(s):
    output_string = ""
    while len(s) > 0:
        last_char = s[-1]
        output_string += last_char
        s = s[:-1]
    return output_string

for index in range(long_string_length - minimum_word_length + 1):
    for j in range(minimum_word_length, long_string_length - index + 1):
        substring = long_string[index:index + j]
        reversed_substring = reverse_string(substring)
        if substring == reversed_substring and len(substring) > len(longest_palindrome):
            longest_palindrome = substring

print("The longest palindromic substring is:", longest_palindrome)