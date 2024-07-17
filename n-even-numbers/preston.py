def main():
    user_input = int(input("Enter the number of even numbers you want: "))
    if user_input < 0:
        print("Please enter a positive number.")
    else:
        even_numbers = []
        count = 0
        current_number = 0
    while count < user_input:
        even_numbers.append(current_number)
        current_number +=2
        count +=1
    print(f"The first {user_input} even numbers are: {even_numbers}")
main()
