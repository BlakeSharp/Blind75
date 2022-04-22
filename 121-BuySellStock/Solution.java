class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int max = 0;
        while(right < prices.length){ 
//all buy low sell high options have been asses when right == len of prices
            if(prices[right]-prices[left] > max){max = prices[right]-prices[left];}
            if(prices[right]-prices[left] <= 0){
//if selling for a loss, that indicates there is a possible better starting point so we need to move the left pointer forward to the position where it sold for less
                left = right;
                right = left+1;
            }
            else{
                right = right + 1;
//because we are still in the profit, we need to see if there is more profit to be had  in the remaining values so we move the right cursor
            }
            
        }
        return max;
        }
}
