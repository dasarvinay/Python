# lambda
# x= lambda : "hello world"
# print(x())

# Dynamic lambda function
# define a function that takes a string and returns the string in uppercase


'''
***
***
***
'''

# for i in range(3):
#     for j in range(3):
#         print("*", end="")
#     print()



for i in range(1,4):
    for j in range(3):
        print(i+j, end='')
    print()


for i in range(1,4):
    for j in range(3):
        print(chr(96+i+j), end="")
    print()

for i in range(1,4):
    for j in range(3):
        print(chr(64+i+j), end="")
    print()
  
x = ('Kbhp', 'Hitech City', 'Maind Space', 'Gachibowli', 'Kondapur')

for x in x:
    if x == "Gachibowli":
        continue
        print(f'{x} reached the bus stop')
        # break
    else:
        print(f'{x} cross the bus stop')



# for i in range(1,20):
#      if i % 3 == 0:
#         continue
#      print(i)










