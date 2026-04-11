class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + f"{len(s)}#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            hash_idx = s.find("#", i)
            word_length = int(s[i: hash_idx])

            start = hash_idx + 1
            end = start + word_length
            word = s[start: end]
            decoded.append(word)

            i = end
        
        return decoded
        
