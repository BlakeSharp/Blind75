class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).upper()
        left, right = 0, len(s)-1
        while(left <= right):
            if(s[left] != s[right]):
                return False
            left+=1
            right-=1
        return True
