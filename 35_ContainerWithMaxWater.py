class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force approach - O(n^2)
        # n = len(height)
        # max_list = []
        # # iterate through the indexes
        # for i in range(n):
        #     for j in range(n-1,i, -1):
        #         # print('i,j', i,j)
        #         sum = (j-i) * min(height[i], height[j])
        #         max_list.append(sum)
        # # print('max list:',max(max_list))
        res = 0
        # two pointers
        left, right = 0, len(height) - 1
        # termination logic
        while left < right:
            max_area = (right - left) * min(height[left], height[right])
            # checking if max_area is greater than res if so assigning it to res
            res = max(res, max_area)
            # if height left < height right
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return res
