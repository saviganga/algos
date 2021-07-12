#!/usr/bin/python3

''' Given a 32-bit signed integer, x, return x with its digits reversed. if reversing string causes the value to go outside the signed 32-bit-integer range [-2**31, 2**31 -1], then return 0 '''

def reverseinteger(num):

    len_num = len( str(num) )

    # check if the number is positive
    if num < 0:

        # turn number to a string
        s_num = str(num)

        # create a list to store reversed string
        r = []
        
        # reverse the string
        while len_num-1 >= 0:
            r.append(s_num[len_num-1])
            len_num -= 1

        # return reversed integer
        return ''.join(r)   

    # nitialize a flag number
    rev = 0

    # solve alogorithm
    while num > 0:

        rev = (rev * 10) + (num % 10)

        num = num // 10
        
    return rev





if __name__ == '__main__':
    num = int(input('Enter a number to reverse it: '))
    nums = reverseinteger(num)
    print(nums)
    
