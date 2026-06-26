def containsDuplicate(self, nums: List[int]) -> bool:
    numberset = set()
    for i in nums:
        if i in numberset:
            return True
        numberset.add(i)
    return False