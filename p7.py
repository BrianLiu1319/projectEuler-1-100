import math
# 50th prime = 229


def check_prime(num):
    for x in range(1,int(math.sqrt(num))):
        if(num % x) == 0:
            return False
    return True


count = 1
prime_list = []
while len(prime_list) != 50:
    if(check_prime(count)):
        prime_list.append(count)
    count += 1
    
#tests 1234
