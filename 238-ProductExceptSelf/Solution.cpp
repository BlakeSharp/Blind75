class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        ans[0] = 1;
        int currProduct = 1;
        
        for(int i = 0; i < n; i++){
            ans[i] = currProduct;
            currProduct = currProduct * nums[i];
        }
        
        currProduct = 1;
        for(int i = n - 1; i >= 0; i--){
            ans[i] = ans[i] * currProduct;
            currProduct = currProduct * nums[i];
        }

        
        return ans;
    }
};