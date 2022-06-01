import math
number = 600851475143
# number = 13195

def prime_factorization(x=number):

    prime_set = set()
    # first start with 2:
    while x % 2 == 0:
        x = x / 2
        prime_set.add(x)

    # now we can iterate upwards

    for i in range(3, int(math.sqrt(x)) + 1):
        while x % i == 0:
            x = x / i
            prime_set.add(i)

    print(max(prime_set))
        
prime_factorization()


# def check_prime(i):

#     for x in range(i + 1):
#         if x % i == 0:
#             return False

#     return True


# for x in range(50):
#     if check_prime(x) == True:
#         print(x)

# for x in reversed(range(number)):
#     if check_prime(x) == True:
#         print(x)
#         break
