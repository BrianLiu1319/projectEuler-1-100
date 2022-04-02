square_sum = 0
sum_of_squares = 0
for x in range(101):
    square_sum += x
    sum_of_squares += x*x
    
square_sum *= square_sum

print(square_sum-sum_of_squares)