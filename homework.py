#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.#

# cube_rt = int(1000 ** 0.334)
#     print(cube_rt)

#     for i in range(14+1):
#         if i > 10:
#             break
#         print(i**3)


# def cubic_printer(num):

#     # Get the square root of a number like so:
#     cube_rt = int(num ** 0.334)

#     print(f'cubic root of num: {cube_rt}')

#     for i in range(cube_rt+1):
#         print(i ** 3)

# # cubic_printer(1000)

# check = 32 ** 2
# print(check)

# Get first prime numbers up to 100

def get_prime(num):

    # Create a list to contain the prime numbers up to num
    primes = []

    # Assume that all numbers in the range up to num are prime,
    # unless proven to be not prime.
    is_prime = True

    # Test all numbers in range(1, num)
    for i in range(1,num):
        # Test all numbers in range of 2 to i//2+1
        # If a number is not divisble by any number up to
        # half of its own size, it will not be a prime number.
        # This is somewhat brute force...
        for j in range(2, i//2+1):
            if i % j == 0:
                # if i is divisble by j, i can't be a prime number.
                # Therefore, is_prime = False.
                is_prime = False
                break
        if is_prime == True:
            # If i was proven to be prime, append it to the
            # list of primes.
            primes.append(i)
        else:
            # If I was proven to not be prime, reset is_prime
            # to equal true so it will be ready for the next loop.
            is_prime = True

    print(primes) # Print the primes list to the console
    return primes # Return the primes list in a functional manner.

get_prime(100) # Test the get_prime() function on 100.
        

# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


answer = int(input('what is your age?'))

if answer < 18:
    print("kids")
elif answer >= 18 and answer <= 65:
    print("adults")
else:
    print("seniors")
