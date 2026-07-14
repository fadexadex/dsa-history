class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for num in arr2:
            if num in arr1:
                while num in arr1:
                    res.append(num)
                    arr1.remove(num)
        new = sorted(arr1)
        return res + new
