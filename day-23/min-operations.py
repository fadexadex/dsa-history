# Day notes: cooking

class Solution:
    def minOperations(self, s: str) -> int:
        alt1 = ""
        alt2 = ""

        for i in range(len(s)):
            if alt1:
                alt1 += "1" if alt1[-1] == "0" else "0"
            else:
                alt1 += "1"
            if alt2:
                alt2 += "1" if alt2[-1] == "0" else "0"
            else:
                alt2 += "0"

        count1 = 0
        count2 = 0
        for i in range(len(s)):
            if s[i] != alt1[i]:
                count1 += 1
            if s[i] != alt2[i]:
                count2 += 1
        return min(count1, count2)
