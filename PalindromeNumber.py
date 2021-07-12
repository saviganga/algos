#!/usr/bin/python3

''' Given an integer x, returntrue if x is a palindrome integer '''

def palindromenumber(nums):
    
    num = nums
    # check if number is greater than 0
    if num < 0:
        return False
    
    # reverse the number
    rev = 0

    while num > 0:

        rev = (rev * 10) + (num % 10)
        num = num // 10

    if nums == rev:
        return True
    else:
        return False

if __name__ == '__main__':
    num = int(input('Enter a number to check if it is a Palindrome: '))
    palin_num = palindromenumber(num)
    print(palin_num)