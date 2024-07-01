user_input = input("Enter a series of digits without dashes: ")

input_list = [int(digit) for digit in user_input]

did_i_change_stuff = True

while did_i_change_stuff:
    did_i_change_stuff = False

    for index in range(len(input_list) - 1):
        if input_list[index] > input_list[index + 1]:
            auxiliary = input_list[index]
            input_list[index] = input_list[index + 1]
            input_list[index + 1] = auxiliary

            did_i_change_stuff = True

sorted_int = int("".join(map(str, input_list)))

print("Sorted digits are:", sorted_int)
