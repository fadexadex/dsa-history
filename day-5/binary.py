
# sub optimal 
def search(self, nums: List[int], target: int) -> int:
    for i in range(0, len(nums)):   O(n)
        if nums[i] == target:  
            return i


# optimal 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1 
            else:
                l = mid + 1
        return -1