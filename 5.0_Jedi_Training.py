  #Sign your name:_Tommy Hensley_

# '''
#  1. Make the following program work.
#    '''
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#         x = input("Enter a number: ")
#         total = total + i
#         print("The total is:", x)
#


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range(0,101,2):
#     print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# countdown = 10
# while countdown > -1:
#     print(countdown)
#     countdown = countdown - 1
# print("Blast Off!")



'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# import random
# value = random.randint(1,10)
# print(value)

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
'''
pos = 0
zero = 0
neg = 0
total = 0
for i in range(7):
    num = int(input("Enter a number"))
    total += num

    if num >= 0:
        pos += 1
    elif num <= 0:
        neg += 1
    else:
        zero += 1

print("The total is: ",total,"!")
print("There were" ,neg, "negative inputs")
print("There were" ,zero, "inputs equal to zero")
print("There were" ,pos, " positive inputs")
'''
'''
