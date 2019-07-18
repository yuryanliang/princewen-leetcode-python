class Solution:
    def maxProfit(self, prices) -> int:

        import sys
        min_price = sys.maxsize
        max_profit = 0

        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)

        return max_profit

def main():
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))


# dp
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [0 for __ in range(len(prices))]
        minPrice = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            if(minPrice > prices[i]):
                minPrice = prices[i]
        return dp[-1]


if __name__ == '__main__':
    main()
