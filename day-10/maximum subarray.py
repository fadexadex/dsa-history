def maxSubArray(self, nums: List[int]) -> int:
    maxVal, currSum = float("-inf"), 0 
    
    for num in nums:
        currSum += num
        maxVal = max(maxVal, currSum)
        if currSum < 0:
            currSum = 0
            
    return maxVal