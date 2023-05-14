import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip all non alphanumeric values
        str1 = s.strip()
        str1 = str1.strip(',')
        str1 = str1.lower()
        str2 = re.sub(r'[^a-zA-Z0-9]', '', str1)
        # print('str2,', str2)
        n = len(str2) - 1
        # check the first and last value if match then push the pointer to next else return False
        for i in range(len(str2)):
            if str2[i] != str2[n]:
                return False
            else:
                n = n -1
        return True
