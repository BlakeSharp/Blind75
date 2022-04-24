class Solution {
    public int[] productExceptSelf(int[] nums) {
        int currProduct = 1;
        int[] arr = new int[nums.length];
        
        for(int i = 0; i < nums.length; i++){
            arr[i] = currProduct;
            currProduct *= nums[i];
        }
        
        currProduct = 1;
        for(int i = nums.length-1; i >= 0 ; i--){
            arr[i] *= currProduct;
            currProduct *= nums[i];
        }
        
        return arr;
    }
}
