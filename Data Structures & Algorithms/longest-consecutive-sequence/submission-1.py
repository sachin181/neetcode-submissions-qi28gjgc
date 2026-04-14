class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        streak_arr = [1]

        if not nums:
            return 0

        for num in nums:
            if (num - 1) not in nums:
                i = 1
                streak = 1
                while num + i in nums:
                    i += 1
                    streak += 1
                
                if streak > 1:
                    streak_arr.append(streak)
        
        return max(streak_arr)




        
        
        
            



        
                


        