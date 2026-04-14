class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        streak_final = 1

        if not nums:
            return 0

        for num in hashset:
            if (num - 1) not in hashset:
                i = 1
                streak = 1
                while num + i in hashset:
                    i += 1
                    streak += 1
                
                if streak > streak_final:
                    streak_final = streak
        
        return streak_final




        
        
        
            



        
                


        