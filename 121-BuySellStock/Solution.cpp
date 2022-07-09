class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int low = 1000000;
        int maxProfit=0;
        for(int i=0; i < prices.size(); i++){
            low = min(low, prices[i]);
            maxProfit = max(maxProfit, prices[i]-low);
        }
        return maxProfit;
    }
};
