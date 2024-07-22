def is_divisible_by_11(number):
    if number % 11 == 0:
        return True
    else:
        return False

def main():
    user_input = int(input("Enter the number of numbers divisible by 11 you want: "))
    if user_input < 0:
        print("Please enter a positive number.")
    else:
        count = 0
        current_number = 1

    while count < user_input:
        if is_divisible_by_11(current_number):
            print(current_number)
            count += 1

        current_number += 1

main()