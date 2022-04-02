number = 600851475143


def check_prime(i):

    for x in range(i + 1):
        if x % i == 0:
            return False

    return True


for x in range(50):
    if check_prime(x) == True:
        print(x)

# for x in reversed(range(number)):
#     if check_prime(x) == True:
#         print(x)
#         break
