# practise functions with syntaxes prperly
# implement perfect number and perfect square logics using functions


def perfect_number(n):
    if n < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

def perfect_square(n):
    if n < 0:
        return False
    i = 0
    while i * i < n:
        i += 1
    return i * i == n


print(perfect_number(28))   
print(perfect_square(25))  
 






