class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""

        for i in range(len(num)):
            if len(result) == 3:
                return result

            if i == 0:
                result += num[i]
            elif num[i] != num[i - 1]:
                result = num[i]
            else:
                result += num[i]

        if len(result) < 3:
            return ""

        return result
