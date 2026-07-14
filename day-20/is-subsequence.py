# Notes (isSubsequence):
# Mistake: checking `c not in t` only tests membership, not order.
# A subsequence must appear in order (not necessarily contiguous).
# Example: s="ace", t="abcde" → True; s="aec", t="abcde" → False
# even though every letter of s appears in t.
# Improvement: use two pointers — advance in t always, advance in s
# only on a match; s is a subsequence iff you consume all of s.


# --- original (incorrect) ---
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         for c in s:
#             if c not in t:
#                 return False
#         return True


# --- corrected ---
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)
