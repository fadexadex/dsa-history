class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        highestcount = 0
        earlycount = 0
        
        for n in nums:
            if n == 1:
                earlycount +=1
                if earlycount > highestcount:
                    highestcount = earlycount
            else:
                earlycount = 0
        
        return highestcount