def is_prime(input_number):
    for i in range(2, input_number):
        if input_number % i == 0:
            return False
    return True
    
number_of_prime_numbers = int(input("Enter the number of prime numbers you want to print: "))
count = 1
current_number = 3

print(2)

while count < number_of_prime_numbers:
    if is_prime(current_number):
        print(current_number)
        count += 1
    current_number += 1