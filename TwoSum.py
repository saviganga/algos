#!/usr/bin/python3

''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. '''

def twosum(nums, target):
    
    # get the length of the array
    nums_len = len(nums)

    # create a dictionary to store the compliment of the sum
    comp = {}

    # loop through the length of the array
    for index, num in enumerate(nums):

        # check if second compliment is present
        if num in comp:
            return [comp[num], index]
        
        # solve the logic
        comp[target - num] = index

    return 0



if __name__ == '__main__':

    nums = [2, 7, 11, 15]
    target = 26

    two_sum = twosum(nums, target)
    print(two_sum)
