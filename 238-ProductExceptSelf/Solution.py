class Solution:
    def productExceptSelf(self, nums):
        currProduct = 1
        arr = []

#This forward traversal puts the product of all numbers behind the current index into its place
        for num in nums:
            arr.append(currProduct)
            currProduct *= num

#Now that the product of all the numbers before the current index are in arr, we can keep a running product of the numbers after it, multiplying the two products and saving that number in the i th place
        currProduct = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i] = arr[i] * currProduct
            currProduct *= nums[i]

        return (arr)
