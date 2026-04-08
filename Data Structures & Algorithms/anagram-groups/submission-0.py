class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       copy = []
       hashM = {}

       for word in strs:
        word = "".join(sorted(word))
        copy.append(word)

       for i in range(len(strs)):
        hashM.setdefault(copy[i], []).append(strs[i])

       return list(hashM.values())
       
       
