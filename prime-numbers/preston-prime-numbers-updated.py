def is_prime(input_number):
    for index in range(len(found_primes)):
        if found_primes[index] * found_primes[index] > input_number:
            break
        if input_number % found_primes[index] == 0:
            return False
    return True

number_of_prime_numbers = int(input("Enter the number of prime numbers to find: "))

# Initialize variables
count = 1
current_number = 3
found_primes = [2]

while count < number_of_prime_numbers:
    if is_prime(current_number):
        found_primes.append(current_number)
        count += 1
    current_number += 1

print(found_primes)