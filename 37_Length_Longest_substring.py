class Solution:
    # O(n2) and space complexity O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max length variable
        maxlen = 1
        if s == '':
            return 0
        # looping through the string to get all the substrings
        for i in range(len(s)):
            substring = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in substring:
                    substring = substring + s[j]
                    # print('substring:', substring)
                    maxlen = max(maxlen, len(substring))
                else:
                    break
        return maxlen
        # d = {}
        # count = 0
        # m = 0
        # for i in s:
        #     if i not in d:
        #         count += 1
        #         d[i] = 1
        #         m = max(m,count)
        #         # print('b:', d)
        #     else:
        #         d = {}
        #         d[i] =1
        #         count = 1
        #     # print('signal:', d)
        # return m
