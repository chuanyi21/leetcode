# Given a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps (self, num: int) -> int:
        stepsCount = 0
        
        while num != 0:
            if(num % 2 == 0):
                num = num / 2
                stepsCount = stepsCount + 1
            else:
                num = num - 1
                stepsCount = stepsCount + 1
        return stepsCount