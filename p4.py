import sys


def is_palindrome(num):

    rev = ''.join(reversed(str(num)))

    if (rev == str(num)):
        return True
    else:
        return False


palindrome_list = []

for x in reversed(range(100, 1000)):
    for y in reversed(range(100, 1000)):
        if is_palindrome(x*y):
            palindrome_list.append(x*y)
            
palindrome_list.sort()

print(palindrome_list[-1])


