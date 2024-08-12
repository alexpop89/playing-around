from datetime import datetime
from math import sqrt


def pretty_print_duration(start_timestamp, end_timestamp):
    duration = end_timestamp - start_timestamp
    total_seconds = duration.total_seconds()
    milliseconds = duration.microseconds

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    print(f"{hours} hours, {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds")

def is_prime(input_number):
    for i in range(2, round(sqrt(input_number))):
        if input_number % i == 0:
            return False
    return True
    
number_of_prime_numbers = int(input("Enter the number of prime numbers you want to print: "))
start_time = datetime.now()

count = 1
current_number = 3

print(2)

while count < number_of_prime_numbers:
    if is_prime(current_number):
        # print(current_number)
        count += 1
    current_number += 1

end_time = datetime.now()

pretty_print_duration(start_time, end_time)