# using  and input()
# print

# "iam karan, came to hyd and joined in 10000 coders for datascience course"

# name = input("Enter the name: ")
# place = input("Enter the  place: ")
# instiute = input("Enter the instiute: ")
# course = input("entger the courses: ")
# p=f"iam {name}, came to {place} and joined in {instiute} for {course} course."
# print(p)


# num = int(input('Enter the value: '))
# reves=0

# while num > 0:
#     digit = num %10
#     reves= reves * 10 + digit
#     num = num // 10
# print(reves)


# prime
# num = int(input('Enter the number: '))

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             print(f"{num} Not a prime number")
#             break
#         else:
#            print(f"{num} It is prime value")


# Palindrome Number

# num = int(input('Enter the number: '))
# pali = num
# res = 0

# while num > 0:
#     digit = num % 10
#     res = res * 10 + digit
#     num = num // 10

# if pali == res:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

# 0. Employee Attendance Tracker: 
# Create a list of employees with present/absent status and print only present employees




# employes = {'vinay':'present', 'kumar':'absent', 'sai':'present', 'raju':'absent'}
# for emp, status in employes.items():
#     if status == 'present':
#         print(emp)  



# Mobile Rating Analyzer: 
# Given a list of mobiles with ratings, print 'Best' (>=4.5), 'Average' (>=3), 'Poor' (<3). 
# mobiles = {'iPhone': 4.8, 'Samsung': 4.2, 'Nokia': 2.5, 'OnePlus': 3.9}
# for mobiles, rating in mobiles.items():
#     if rating >=4.5:
#         print(f"{mobiles}: {rating}", 'Best')
#     elif rating >=3:
#         print(f"{mobiles}: {rating}", 'Average')
#     else:
#         print(f"{mobiles}: {rating}", 'Poor')


# . Bus Ticket System: 
# Input age and print: 
# <5 → Free 
# 5–60 → Full Ticket 
# >60 → Discount 


# age= int(input('Enter the age: '))
# if age < 5:
#     print(f'{age} Free bus')
# elif age >= 5 and age < 60:
#     print(f'{age} Full Ticket ')
# else:
#     print(f'{age} Discount bus')


#  Digit Frequency Counter: 
# Write a program to count how many times each digit appears in a number. 
# Example: Input: 112233 → Output: {1:2, 2:2, 3:2} 
    

# num = input('Enter the number: ')
# fer ={}

# for digit in num:
#     if digit in fer:
#         fer[digit] += 1
#     else:
#         fer[digit] = 1          
# print(fer)


# Swap two numbers (without temp variable)
# a=5
# b=6
# a=a+b
# b=a-b
# a=a-b

    

