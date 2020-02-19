# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Time Complexity: O(N)
#Space Complexity: N

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        result = []
        
        for x in range(len(nums)):
            if (target - nums[x]) in d1:
                return [x,d1[target - nums[x]]]
            
            else:
                d1[nums[x]] = x