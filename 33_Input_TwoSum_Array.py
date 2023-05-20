class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l = []
        # n = len(numbers)
        # iterate over the list twice and check the sum of one constant and other changing if found break return list
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if numbers[i] + numbers[j] == target:
        #             l.extend((i+1,j+1))
        #             break
        #     if l:
        #         break
        # return l

        #method ii pointers and while loop
        input_list = []
        start = 0
        end = len(numbers) - 1

        # iterate from start to end of array to check target sum
        while start < end:
            if target == numbers[start] + numbers[end]:
                return (start +1, end +1)
            elif target < numbers[start] + numbers[end]:
                end -= 1
            else:
                start += 1

                
