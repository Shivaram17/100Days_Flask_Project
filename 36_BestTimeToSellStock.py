# Memory : O(1) and time: O(n) two pointer method
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #result to store
        res = 0
        left = 0
        right = 1
        #using two pointer method
        while right < len(prices):
            print('prices right:', right)
            if prices[left] < prices[right]:
                max_sum = prices[right] - prices[left]
                res = max(res, max_sum)
                # print('max_sum:', res)
            else:
                left = right
            right +=1

        # # use two conditions to get the 
        # while left < right:
        #     # check prices left > prices right
        #     if prices[left] > prices[right]:
        #         # shift left + and right -1
        #         if prices[left] > prices[left + 1]:
        #             left +=1
        #         else:
        #             right -=1
        #     elif prices[left] <= prices[right]:
        #         max_sum = prices[right] - prices[left]
        #         res = max(res, max_sum)
        #         while res < (prices[right-1] - prices[left]):
        #             max_sum = prices[right-1] - prices[left]
        #             res = max(res, max_sum)
        #             right -=1
        #         # shift left + and right -1
        #         if prices[left] > prices[left + 1]:
        #             left +=1
        #         else:
        #             right -=1
        return res
