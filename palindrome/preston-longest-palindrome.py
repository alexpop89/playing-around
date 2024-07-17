long_string = input("Enter a string: ")

long_string_length = len(long_string)
minimum_word_length = 2
longest_palindrome = ""


def has_alphabetical_letters(str_value, how_many = 3):
    count = 1
    for index in range(len(str_value) - 1):
        if str_value[index] < str_value[index + 1]:
            count += 1
            if count == how_many:
                return True
        else:
            count = 1

    return False


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
        if substring == reversed_substring and len(substring) > len(longest_palindrome) and has_alphabetical_letters(substring, 3):
            longest_palindrome = substring

print("The longest palindromic substring is:", longest_palindrome)