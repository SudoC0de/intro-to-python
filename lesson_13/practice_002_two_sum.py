# Given an array of integers, nums, and an integer target, return two numbers such
# that they add up to target.
# Assume there’s only one unique pair of numbers that will sum up to the target and
# you may not use the same element twice.
# You can return the answer in any order.
# Example:
# Input: nums = [1, 2, 3, 7, 5], target = 10
# Output: [3, 7]

def two_sum(arr, target):
    if len(arr) < 2:
        return

    sum_dict = {}

    for num in arr:
        num_add = target - num

        if num_add in sum_dict:
            return [num, num_add]
        else:
            sum_dict[num] = True

print(two_sum([1, 2, 3, 7, 5], 10))
