#find the sum of all elements in a given list at numbers

# sum = [10, 20, 30, 40, 50]
# total = 0
# for i in sum:
#     total += i
# print("Sum of all elements:", total)


#find the maximum and minimum values in a list at number

# num = [15,2, 7, 25, 10]

# max = num[0]
# min = num[0]

# for i in num:
#     if max < i:
#         max = i
#     elif min > i:
#         min = i

# print("Maximum value:", max)
# print("Minimum value:", min)


# remov duplicates from a list to create a new list with unique elements

# number = ['10', '20', '30', '20', '40', '10', '50']

# unique_elements = []
# for i in number:
#     if i not in unique_elements:
#         unique_elements.append(i)
# print("Unique elements:", unique_elements)


# num = [1,2,3,2,1,4,2,5]

# count = 0
# for i in num:
#     if i == 2:
#         count += 1
# print("Count of 2:", count)

# Find second largest in list (without sort).
# num = [10, 20, 5, 30, 25]
# largest = num[0]
# second_largest = num[0]
# for i in num:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i

# print("Second largest value:", second_largest)


#Create dictionaries, access values, upadte values, and iterate through key-value pairs

# my_dict = {'name': 'vinay', 'age': 30, 'city': 'Warangal'}

# my_dict['age']= 31
# my_dict['city']= "Hyderabad"
# print(my_dict)



# check whether num is leap year or not

# def is_leap(year):
#     leap = False
#     if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return leap
# year = int(input('Enter the year: '))
# print(is_leap(year))

# year = int(input('Enter the year: '))
# if(year % 4 ==0 and year % 100 !=0) or (year % 400 == 0):
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')


# num = 123
# rev = 0

# while num != 0:
#     rev = rev *10 + num % 10
#     num //= 10

# print(rev)




#generate electricity bill as per the units
# """
# for first 100 units--->2rs/unit
# next 100 units--->3rs/unit
# above 200 units-->5rs unit

# def calculate_bill(units):
#     if units <= 100:
#         bill = units * 2
#     elif units <= 200:
#         bill = 100 * 2 + (units - 100) * 3
#     else:
#         bill = 100 * 2 + 100 * 3 + (units - 200) * 5
#     return bill
# units = int(input("Enter the number of units consumed: "))
# total_bill = calculate_bill(units)
# print(f'Total electricity bill: {total_bill}')


# a+b+c = 180 its a trinagle
# a==b==c =180 equaltrial trinagle
# a==b or b==c or a==c isosceles trinagle

# a = int(input("Enter the first angle of the triangle: ")) 
# b = int(input("Enter the second angle of the triangle: ")) 
# c = int(input("Enter the third angle of the triangle: ")) 

# if a + b + c == 180:
#     if a == b == c:
#         print("It is an equilateral triangle.")
#     elif a == b or b == c or a == c:
#         print("It is an isosceles triangle.")
#     else:
#         print("It is a scalene triangle.")
# else:
#     print("The given angles do not form a valid triangle.")




# Given an array of numbers, return the difference between the maximum and minimum values.
# Example 1
# Input: [4, 2, 7, 1]

# Output: 6

# Explanation:

# max = 7
# min = 1
# difference = 7 − 1 = 6


# print something is fishy

# i need to get out put 
#
# str1 = 'SOMETHING IS FISHY'
# X =1 
# for char in str1:
#     print(char, str1[x])
#     x +=1





#out put
# D-hello
# A- hello
# T - hello
# A - hello

# str1 = 'DATA'
# x= 'Hello'

# for i in str1:
#     print(i,x, sep='-')




# list1 = [4, 6, 8, 2, 3, 1, 8, 9]

# 0
#6
#16
# for i in list1:
#     # print(f"{i * list1.index(i)}")


#     print(i * list1.index(i))

# for i in list1:
#     print(f"Square of {i} is {i**2}")



# list1 = ['shiva', 'vinay', 'deepak', 'saketh', 'satwik']

# for name in list1:
#     print(f"{name} length is {len(name)}")



# str1 = 'BANANA'


# dict1 = {}
# for x in str1:
#     if x in dict1:
#         dict1[x] += 1
#     else:
#         dict1[x] = 1
# print(dict1)


# a= ['apple', 'BANANA', 'cherry', 'DATE', 'fig', 'GRAPE']

# UPPER CASE= LOWER CASE
# LOWER CASE= UPPER CASE

# for item in a:
#     if item==item.upper():
#         print(item.lower())
#     else:
#         print(item.upper())


# s1='soMeTHIng'

# for i in s1:
#     if i == i.upper():
#          print(i.lower())
#     else:
#         print(i.upper())

# for i in s1:
#     if i == i.upper():
#         op += i.lower() 
#     else:
#         op += i.upper()
# print(op)
    #     print(i.lower())
    # else:       
    #     print(i.upper())
        


#find the factorial of a number
# num = 5
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"Factorial of {num} is {factorial}")



# ecommerce_data = [
#     {
#         "order_id": "O1001",
#         "customer_name": "Ravi Kumar",
#         "city": "Hyderabad",
#         "product": "Wireless Mouse",
#         "category": "Electronics",
#         "price": 799,
#         "quantity": 2,
#         "total_amount": 1598,
#         "payment_method": "UPI",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1002",
#         "customer_name": "Sneha Reddy",
#         "city": "Bangalore",
#         "product": "Bluetooth Headphones",
#         "category": "Electronics",
#         "price": 1999,
#         "quantity": 1,
#         "total_amount": 1999,
#         "payment_method": "Credit Card",
#         "order_status": "Shipped"
#     },
#     {
#         "order_id": "O1003",
#         "customer_name": "Arjun Singh",
#         "city": "Mumbai",
#         "product": "Running Shoes",
#         "category": "Fashion",
#         "price": 2499,
#         "quantity": 1,
#         "total_amount": 2499,
#         "payment_method": "Cash on Delivery",
#         "order_status": "Processing"
#     },
#     {
#         "order_id": "O1004",
#         "customer_name": "Priya Sharma",
#         "city": "Delhi",
#         "product": "Smart Watch",
#         "category": "Electronics",
#         "price": 3499,
#         "quantity": 1,
#         "total_amount": 3499,
#         "payment_method": "Debit Card",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1005",
#         "customer_name": "Kiran Patel",
#         "city": "Chennai",
#         "product": "Laptop Backpack",
#         "category": "Accessories",
#         "price": 1299,
#         "quantity": 3,
#         "total_amount": 3897,
#         "payment_method": "UPI",
#         "order_status": "Shipped"
#     }
# ]



