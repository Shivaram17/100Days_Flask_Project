#Binary search
# Find Minimum in rotated sorted array
class Solution:
    def findMin(self, nums):
        for i in range(len(nums)-1):
          if nums[i+1] < nums[i]:
            return nums[i+1]
        return nums[0]

# nums = [11,12,13,14,1,2,3]
# nums = [1,2,3]
# nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]
obj = Solution()
output = obj.findMin(nums)
output
