'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_ind, i in enumerate(nums):
            for j_ind, j in enumerate(nums):
                if i_ind != j_ind and i + j == target:
                    return [i_ind, j_ind]