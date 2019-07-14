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


if __name__ == '__main__':
    main()
