class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, maxLen, usedChar = 0 , 0 , {}

        for i in range(0, len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1

            else:
                maxLen = max(maxLen, i - start + 1)

            usedChar[s[i]] = i

        return maxLen
