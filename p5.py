def even_div(num):
    for x in range(2,20):
        if (num % x) != 0:
            return True
    return False

num = 2520


while even_div(num):
    num += 20
    
print(num)