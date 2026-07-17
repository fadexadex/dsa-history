class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        if len(arr) < k:
            return ""

        count = 0
        result = ""

        d = {}
        for s in arr:
            d[s] = d.get(s, 0) + 1

        if len(d) < k:
            return ""

        for key, v in d.items():
            if count == k:
                return result

            if v == 1:
                count += 1
                result = key

        return result
