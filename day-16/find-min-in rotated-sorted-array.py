def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    s = float('inf')

    if nums[r] > nums[l]:
        return nums[l]


    while l < r:        
        mid = (l + r) // 2
        if nums[l] < nums[mid] or nums[r] < nums[mid]:
            s = nums[r] if nums[r] < nums[l] else nums[l]
        else:
            if s > nums[mid]:
                s = nums[mid]
        l = mid + 1
            
# [3,4,5,1,2]