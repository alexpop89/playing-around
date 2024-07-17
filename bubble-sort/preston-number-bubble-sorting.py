input_list = [-1, 8, -4, 0, 9, 10]

did_i_change_stuff = True

while did_i_change_stuff:
    did_i_change_stuff = False

    for index in range(len(input_list) - 1):
        if input_list[index] < input_list[index + 1]:
            auxiliary = input_list[index]
            input_list[index] = input_list[index + 1]
            input_list[index + 1] = auxiliary

            did_i_change_stuff = True

print("List: " + str(input_list))
