input_string = "example_string"
output_string = ""

while len(input_string) > 0:
    last_char = input_string[-1]
    output_string += last_char
    input_string = input_string[:-1]

print(output_string)