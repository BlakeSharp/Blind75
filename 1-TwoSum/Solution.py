class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedElements  = {}
        for number  in range(0,len(nums)):
            if nums[number] in visitedElements:
                return [thing[nums[el:em]],elem]
            else:
                thing[target-nums[elem]] = elem


