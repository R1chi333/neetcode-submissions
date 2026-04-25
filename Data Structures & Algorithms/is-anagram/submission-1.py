from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if dict(Counter(s)) == dict(Counter(t)):
            return True
        else:
            return False