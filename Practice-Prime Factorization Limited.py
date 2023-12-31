# Predefined list of prime numbers up to 100
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Function to calculate prime factors of a number using the provided prime numbers list
def prime_factors(n):
    factors = []
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return factors

# Insert function to calculate LCM

#def calculate_lcm(a,b)
#   prime_factors_a = prime_factors(a)
#   prime_factors_b = prime_factors(b)
#   all_factors = prime_factors_a + prime_factors_b
# Insert code for powers


# Prompt user to input two positive whole numbers separated by commas
numbers_input = input("Enter two positive whole numbers separated by commas to find the LCM: ")
numbers_list = numbers_input.split(",")

# Extract and convert the input numbers
number_one = int(numbers_list[0].strip())
number_two = int(numbers_list[1].strip())

# Calculate prime factors for each input number
prime_factors_one = prime_factors(number_one)
prime_factors_two = prime_factors(number_two)

# Print the input numbers and their respective prime factors
print("For", number_one, ", these are all prime factors:", prime_factors_one)
print("For", number_two, ", these are all prime factors:", prime_factors_two)
