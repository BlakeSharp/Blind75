class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for value in nums:
            if(value in visited):
                return True
#Check if the value exists in the dictionary
            else:
                visited[value] = 1
#input a placeholder value to allow for constant look up time
        return False
