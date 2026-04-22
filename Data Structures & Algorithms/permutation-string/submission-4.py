class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = {}
        word_count = {}

        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            letters[s1[i]] = letters.get(s1[i], 0) + 1
            word_count[s2[i]] = word_count.get(s2[i], 0) + 1

        for i in range(len(s2)):
            j = i + len(s1) - 1

            if j > len(s2) - 1:
                return False

            if i != 0:
                word_count[s2[j]] = word_count.get(s2[j], 0) + 1

            if letters == word_count:
                return True
            
            word_count[s2[i]] -= 1 

            if word_count[s2[i]] == 0:
                del word_count[s2[i]]

        return False


            
        

        
        




        
        
        