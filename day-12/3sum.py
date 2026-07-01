def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    
    for i in range(len(nums) - 1):
        a = nums[i]
        small = nums[i + 1: len(nums)].sort()

        l, r = 0, len(small)
        while l < r:
            s = small[l] + small[r]
            if s == -a:
               result.append([nums[i], nums[l], nums[r]])
            elif s < -a:
                r -= 1
            else:
                l += 1

    return result    



# result = []     i = 0, small = [0,1,2,-1, -4]
#                    l =0 -> 1 -> 2, r = 5 -> 4 -> 3 -> 2
#                    s = 0 + -4 = -4
#                     s = 0 + -1 = -1
#                    s = 1 + -1 = 0
#                     s = 1 + 2 = 3
            
            
            