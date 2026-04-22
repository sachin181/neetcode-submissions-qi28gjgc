class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = {}
        

        for i in range(len(s2)):
            j = i + len(s1) - 1
            if j < len(s2) and sorted(s1) == sorted(s2[i:j + 1]):
                return True
                
        return False




        
        
        