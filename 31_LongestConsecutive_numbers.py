class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if array is empty return 0
        if not nums:
            return 0
        count = 1
        store = 0
        # final_list = list(set(nums))
        # final_list = []
        # [final_list.append(i) for i in nums if i not in final_list]
        #sort the array
        final_list = sorted(nums)
        print(final_list)
        #iterate through the array and get the difference between each consecutive numbers if it is 1 then count + 1 else stor maximum count
        for i in range(len(final_list) - 1):
            if final_list[i] != final_list[i+1]:
                if (final_list[i+1] - final_list[i] == 1):
                    count = count + 1
                else:
                    store = max(store, count)
                    count = 1
        return max(store, count)
