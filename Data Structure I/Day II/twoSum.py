# Given an array of integers nums and an integer target, return indices of 
# the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_ind in range(len(nums)):
            for sec_ind in range(len(nums)):
                if first_ind == sec_ind:
                    continue
                elif nums[first_ind] + nums[sec_ind] == target:
                    return [first_ind, sec_ind]