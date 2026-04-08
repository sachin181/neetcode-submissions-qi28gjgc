class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        for letter in s:
            if not letter.isalnum():
                s = s.replace(letter, "")
        s = s.lower()

        return s == s[::-1]
