class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedElements  = {}
        for index, number  in enumerate(nums):
            if number in visitedElements:
                return [visitedElements[number], index]
            else:
                visitedElements[target-number] = index
