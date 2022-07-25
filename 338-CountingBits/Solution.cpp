class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans;
        for(int i = 0; i <= n; i++){
            int curr = i;
            int count = 0;
            while (curr){
                count += curr%2;
                curr >>= 1;
            }
            ans.push_back(count);
        }
        return ans;
    }
};
