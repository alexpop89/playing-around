long_string = "Preston"
long_string_length = len(long_string)
minimum_word_length = 2

for index in range(long_string_length - minimum_word_length):
    for j in range(minimum_word_length, long_string_length - index + 1):
        substring = long_string[index:index + j]
        print(substring)
