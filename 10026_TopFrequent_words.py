import itertools
class Solution:
  
    def topKFrequent(self, nums, k):
      nums_sort = sorted(nums)
      count = 1
      l = []
      d = {}
      for item in nums_sort:
        if item in d:
          d[item] += 1
        else:
          d[item] = 1
      # sorted_dict = sorted(d, key = d.get, reverse = True)
      print(d)
      # find the top frequent digits
      for w in sorted(d, key = d.get, reverse = True):
        l.append(w)
      return l[:k]

# Invoking a class
# nums = [1,1,1,2,2,3]
# nums = [1]
nums = [3,0,1,0]

k = 1
obj = Solution()
obj.topKFrequent(nums, k)
