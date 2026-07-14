import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            maxPile = max(gifts)
            newPile = math.floor(math.sqrt(maxPile))
            gifts[gifts.index(maxPile)] = newPile

        return sum(gifts)
