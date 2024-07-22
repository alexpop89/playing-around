def is_divisible_by_11(number):
    if number % 11 == 0:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if is_divisible_by_11(number):
    print(f"{number} is divisible by 11.")
else:
    print(f"{number} is not divisible by 11.")