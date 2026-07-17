class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sub = 0
        total = 0
        for i in range(len(nums)):
            if i == 0:
                total += nums[i]
            elif nums[i - 1] < nums[i]:
                total += nums[i]
            else:
                total = nums[i]
            max_sub = max(max_sub, total)
        return max_sub
