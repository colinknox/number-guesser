#!/usr/bin/python3

def count_until(target):
    number = 0
    
    while number < target:
        number += 1
        print(number)

def count_down_until(start, stop):
    while start >= stop:
        print(start)
        start -= 1

def double_until_over(start, limit):
    while start <= limit:
        print(start)
        start *= 2

def count_by_n_until(start, step, limit):
    while start <= limit:
        print(start)
        start += step



# # count_until() TEST
# count_until(10)
# count_until(5)
# count_until(20)

# # count_down_until() TEST
# count_down_until(10, 1)
# count_down_until(18, 3)
# count_down_until(30, 25)

# # double_until_over() TEST
# double_until_over(5, 100)
# double_until_over(10, 1000)
# double_until_over(2, 25)

# # count_by_n_until() TEST
# count_by_n_until(1, 5, 25)
# count_by_n_until(5, 2, 50)
# count_by_n_until(0, 10, 74)