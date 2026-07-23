class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bigg = 0
        for i in range(len(prices)-1, 0, -1):
            prof = prices[i] - min(prices[:i])
            if prof > bigg:
                bigg = prof
        return bigg
