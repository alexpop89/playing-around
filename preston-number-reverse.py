input_number = 8909876621
output_number = 0

while input_number > 0:
    digit = input_number % 10
    output_number = output_number * 10 + digit
    input_number = input_number // 10

print(output_number)
