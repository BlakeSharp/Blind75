class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in t:
            try:
                counts[char]+=1
            except:
                counts[char] = 1
        for char in s:
            if char not in counts:
                return False
            if counts[char] > 0:
                counts[char] -= 1
                continue
            return False
        for key in counts:
            if(counts[key]>0):
                return False
        return True
