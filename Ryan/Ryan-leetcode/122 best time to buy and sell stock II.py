class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

def main():
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))


if __name__ == '__main__':
    main()
