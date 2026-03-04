



# a = int(input("Enter the a value: "))
# b = int(input("Enter the b value: "))

# def sum_num(a, b):
 
#  sum_num (a + b)
#     # return a+b

# # res = sum_num(10, 20)

# print(sum_num(a,b))



# def radius_circle(r):
#     return 3.14* r **2
# res = radius_circle(5)

# print(res)

# def radius_circle(r):
#     return 3.141* r **2
# radius = float(input('enter the radius of cricle: '))
# result=radius_circle(radius)
# print(f'Area of the cricle: {result}')


# def is_leap(year):
#     leap = False
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return leap
# year = int(input("Enter the year"))
# print(is_leap(year))


# swap the values of two variables without using temporary variables use functions
# def swap_values(a, b):
#     a, b = b, a
#     return a, b

# x = 10
# y = 20
# x, y = swap_values(x, y)
# print(f"After swapping: x = {x}, y = {y}")



# task:
# --------
#write a function which calculates movie tickets price and returns
#gift as per billing amount
#if amount is greater than 2000 then return coke+popcorn
#if amount id greater than 1500 then return coke
#if amount is less than 1500 then say thankyou

def movie_ticket(ticket_price, num_ticket):
    total_price = ticket_price * num_ticket

    if total_price > 2000:
        return 'coke + popcorn'
    elif total_price > 1500:
        return 'coke'
    else:
        return 'Thank you for booking tickets'

ticket_price = float(input('Enter the ticket price: '))
num_ticket = int(input('Enter the number of tickets: '))

total = ticket_price * num_ticket
result = movie_ticket(ticket_price, num_ticket)

print(f'Total billing amount: {total}, Gift: {result}')

