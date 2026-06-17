   # sub optimal 
   
    def missingNumber(self, nums: List[int]) -> int:
        M = len(nums)
        n = M + 1

        for i in range(0, n):
            if i not in nums:
                return i   

    def missingNumber(self, nums: List[int]) -> int:
        # optimal solution
        res = len(nums)
            
        for i in range(len(nums)):
            res += (i - nums[i])
            print(res)
        return res