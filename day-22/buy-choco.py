class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        price_sum = prices[0] + prices[1]
        if price_sum > money:
            return money
        return money - price_sum
