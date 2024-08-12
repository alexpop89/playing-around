from datetime import datetime


def pretty_print_duration(start_timestamp, end_timestamp):
    duration = end_timestamp - start_timestamp
    total_seconds = duration.total_seconds()
    milliseconds = duration.microseconds

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    return f"{hours} hours, {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds"

def sieve_of_eratosthenes(n):
    if n < 1:
        return []

    primes = []
    limit = 100  # Initial limit, adjust if needed
    while len(primes) < n:
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
        for start in range(2, int(limit ** 0.5) + 1):
            if sieve[start]:
                for multiple in range(start * start, limit + 1, start):
                    sieve[multiple] = False
        primes = [num for num, is_prime in enumerate(sieve) if is_prime]
        limit *= 2  # Increase the limit if not enough primes are found

    return primes[:n]

# Example usage
number_of_prime_numbers = int(input("Enter the number of prime numbers to find: "))

start_time = datetime.now()


first_n_primes = sieve_of_eratosthenes(number_of_prime_numbers)

end_time = datetime.now()

total_time = pretty_print_duration(start_time, end_time)
print(first_n_primes)
print(total_time)