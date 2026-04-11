class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        result = [0] * len(nums)
        n = len(nums)
        
        #prefix array
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]

        #suffix array
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
    
        #Calculate product
        for i in range(n):
            result[i] = prefix[i] * suffix[i+1]
        
        return result
        
        


        
        
        
        
            
        
        