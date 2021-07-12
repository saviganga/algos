#!/usr/bin/python3

''' Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays'''

def medianoftwosortedarrays(nums1, nums2):

    # merge the two lists together
    merged_list = sorted([*nums1, *nums2])

    # find the length of the joined list
    len_merged_list = len(merged_list)

    # if length of joined array odd...
    if len_merged_list % 2 != 0:
        median_index = len_merged_list // 2
        median = merged_list[median_index]
        return median

    # else, if even...
    else:
        first_index = int(len_merged_list / 2)
        next_index = int(first_index + 1)
        median = ( merged_list[first_index-1] + merged_list[next_index-1] ) / 2
        return median


if __name__ == '__main__':
    nums1 = []
    nums2 = [1]
    m = medianoftwosortedarrays(nums1, nums2)
    print(m)