class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # method2
        n = len(nums)
        prefix_prod = [0]*n
        suffix_prod = [0]*n
        product = [0]*n

        # prefix 
        prefix_prod[0] = 1
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        print('prefix: ', prefix_prod)
        #suffix
        suffix_prod[n-1] = 1
        for j in range(n-2, -1, -1):
            suffix_prod[j] = suffix_prod[j+1] * nums[j+1]
        
        print('suffix: ', suffix_prod)
        #final product
        # prefix_and suffix to product excetp productExceptSelf
        for i in range(n):
            product[i] = prefix_prod[i] * suffix_prod[i]
        
        return product
        # method1
        # prod = 1
        # prod_list = []
        # #iterating through for loops
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[j]==0:
        #                 prod = 0
        #                 break
        #             else:
        #                 prod = prod * nums[j]
        #         else:
        #             continue
        #     prod_list.append(prod)
        #     prod = 1
        # print(prod_list)
        # return prod_list
