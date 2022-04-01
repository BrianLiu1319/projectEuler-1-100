def fibonnacci(first_term, second_term):
    return first_term + second_term


sum = 0
first = 1
second = 2

while first < 4000000:
    if first % 2 == 0:
        sum += first
    temp = first
    first = second
    second = fibonnacci(temp, second)

print(sum)
