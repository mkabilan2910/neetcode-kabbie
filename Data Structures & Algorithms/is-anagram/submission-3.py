class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(0,len(s)+1):
            if len(s)==len(t):
                if sorted(s)==sorted(t):
                    return True
            return False