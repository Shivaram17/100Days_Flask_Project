class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a hashmap
        count = {}
        result = 0

        l = 0
        for r in range(len(s)):
            # updating the hashmap
            count[s[r]] = 1 + count.get(s[r], 0)
            # check if length of window - count of most frequent word in the window is < k
            while (r - l +1) - max(count.values()) > k:
                # reduce the count of the 
                count[s[l]] -= 1
                l += 1
            
            # result 
            result = max(result, r-l + 1)
        return result
