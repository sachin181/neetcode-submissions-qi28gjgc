class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans_list = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            start = i + 1
            end = len(nums) - 1

            while start < end:
                if nums[start] + nums[end] == target:
                    if ([nums[i], nums[start], nums[end]]) not in ans_list: 
                        ans_list.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    start += 1
                
            

        return ans_list





        