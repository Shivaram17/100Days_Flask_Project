# Product of Arrays except self
# !pip install list
# import list
class Solution:
  def productExceptSelf(self, nums):
    prod = 1
    prod_list = []
    #iterating through for loops
    for i in range(len(nums)):
      for j in range(len(nums)):
          if i != j:
              if nums[j]==0:
                  prod = 0
                  break
              else:
                prod = prod * nums[j]
          else:
              continue
      prod_list.append(prod)
      prod = 1
    print(prod_list)
    return prod_list

# initialising the class
if __name__ =="__main__":
  # nums = [-1,1,0, 1,3,4]
  nums = [0,0,1]

  obj = Solution()
  obj.productExceptSelf(nums)
