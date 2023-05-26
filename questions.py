# Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(username):
    username = input("Enter your username ")
    print("hello_" + username.upper())
    
hello_name("")
    
    
# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds(numbers):
  for num in numbers:
    num == num+1 
    print(num)

odd_numbers = range(1 , 100, 2)

first_odds(odd_numbers)


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):   
   max_num_in_list = max(a_list)

a_list = max (1, 0, 100, 1000, 355, 799, 8000)
print(a_list)


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')

is_leap_year(2019)
    

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    a_list.sort()
    for num in range(len(a_list) - 1):
        if a_list[num] + 1 != a_list[num + 1]:
            return False
    return True
a_list = [3,1,2,4, 6, 5]

print(is_consecutive(a_list))

