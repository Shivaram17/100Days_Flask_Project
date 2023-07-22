class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        matches = 0
        # check if len(Sttr1) < len(str2)
        if len(s1) > len(s2):
            return False
        
        # create two arrays with ascii values
        s1_count, s2_count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            # print('s1_count',s1_count,end='\n')
            # print('s2_count', s2_count)
        #create variable which stores matches
        # 
        left  = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)
            # print('matches: ', matches)
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index]  == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -=1

            left += 1

        return matches == 26
