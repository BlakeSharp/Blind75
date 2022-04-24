    class Solution:
        def findMin(self, nums: List[int]) -> int:
            left = 0
            right = len(nums)-1

    #binary search for the min number

            while(left < right):
                if(nums[(right+left)//2] > nums[right]):
                    left = ((right+left)//2)+1

                else:
                    right = (right+left)//2

            return nums[left]
