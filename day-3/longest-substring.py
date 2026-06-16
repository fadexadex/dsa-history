class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length = len(s)
        max_length = 0
        char_set = set()

        while r < length:
            
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            max_length = max(r - l + 1, max_length)
            r += 1
        return max_length