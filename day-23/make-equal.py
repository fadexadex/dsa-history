# Day notes: cooking

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count_map = {}
        for word in words:
            for c in word:
                count_map[c] = count_map.get(c, 0) + 1

        for total in count_map.values():
            if total % len(words) != 0:
                return False

        return True
