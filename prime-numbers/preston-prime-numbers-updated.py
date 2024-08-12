from datetime import datetime


def pretty_print_duration(start_timestamp, end_timestamp):
    duration = end_timestamp - start_timestamp
    total_seconds = duration.total_seconds()
    milliseconds = duration.microseconds

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    print(f"{hours} hours, {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds")


def is_prime(input_number):
    for index in range(len(found_primes)):
        # print(f'{index}/{len(found_primes)}')
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

start_time = datetime.now()

while count < number_of_prime_numbers:
    if is_prime(current_number):
        found_primes.append(current_number)
        count += 1
    current_number += 1

end_time = datetime.now()
pretty_print_duration(start_time, end_time)

print(found_primes)