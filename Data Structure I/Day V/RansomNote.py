from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote)-Counter(magazine) == {}        


ransomNote = "aa"
magazine = "aab"
solution = Solution()
solution.canConstruct(ransomNote=ransomNote, magazine=magazine)