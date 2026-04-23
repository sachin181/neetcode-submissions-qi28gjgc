class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxval = 0

        l = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            maxval = max(maxval, count[s[r]])

            if (r - l + 1) - maxval > k:
                count[s[l]] -= 1
                l += 1
            
        return r - l + 1

        