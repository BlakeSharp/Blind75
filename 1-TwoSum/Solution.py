class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedElements  = {}
        for number  in range(0,len(nums)):
            if nums[number] in visitedElements:
                return [visitedElements[nums[number]],number]
            else:
                visitedElements[target-nums[number]] = number
