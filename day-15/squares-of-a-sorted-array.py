def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        for n in nums: 
           n= n**2
           answer.add(n) 
        answer.sort()
        
#      O(nlogn) 
# 1 square the num in the nums array
# 2. then sort the answer

# Best method

def sortedSquares (self, nums: List[int]) -> List[int]:
    l, r = 0, len (nums) -1
    res = []
    while l <= r:
        if nums [l]**2 > nums [r]**2: 
            res. append (nums [l]**2)
            l += 1
        else:
            res. append (nums [r]**2)
            r -= 1
    return res [::-1]
