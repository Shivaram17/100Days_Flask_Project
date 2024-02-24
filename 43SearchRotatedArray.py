#Binary Search
#Search rotated array
class Solution:
    def search(self, nums, target):
      if target in nums:
        for i in range(len(nums)):
          if target == nums[i]:
            output = i
            return output
      else:
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
# nums = [1]
# target = 1
obj = Solution()
output = obj.search(nums, target)
output
