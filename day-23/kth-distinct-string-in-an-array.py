# Day notes: cooking

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = Counter(arr)
        unique_count = 0
        for i in range(len(arr)):
            if unique[arr[i]] == 1:
                unique_count += 1
                if unique_count == k:
                    return arr[i]

        return ""
