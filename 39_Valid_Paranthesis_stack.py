class Solution:
    def isValid(self, s: str) -> bool:
         # list1 and list2
        l1 = ['(', '{','[']
        l2 = [')', '}', ']']
        #  out = []
        # dictionary
        d = {'(':')', '{':'}', '[':']'}
        if len(s) > 1:
            out = []
            for i in s:
                if i in l1:
                    # print(i)
                    out.append(i)
                    # print(out)
                elif i in l2:
                    if out != []:
                        if d[out[-1]] == i:
                            out.pop()
                        else:
                            return False
                    else:
                        return False
            # if my out_list is empty then return True
            if out == []:
                return True
            else:
                return False
        else:
            return False
# instantiate the class
# s = '({[]})'
# s = ''
s = "){"
obj = Solution()
obj.isValid(s)
