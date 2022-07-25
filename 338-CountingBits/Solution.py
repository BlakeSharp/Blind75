class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for elem in range(n+1):
            ans.append(bin(elem).count('1'))
        return ans
