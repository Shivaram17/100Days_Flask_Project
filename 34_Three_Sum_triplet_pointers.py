class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        # sort the arr
        # nums = sorted(nums)
        nums.sort()
        print('sorted array: ', nums)
        n = len(nums)
        triplets = []
        for i in range(0, n):
            #avoid duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            # left and right pointers
            j = i + 1
            k = n -1

            # loop through the remaining pairs
            while j < k:

                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j +=1
                    #avoid duplicates
                    while j<k and nums[j] == nums[j-1]:
                        j +=1
                
                elif sum < 0:
                    j +=1
                else:
                    k -=1

        return triplets
            
