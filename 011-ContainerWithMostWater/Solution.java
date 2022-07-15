class Solution {
    public int maxArea(int[] height) {
        if(height.length == 2 ){
            return height[0] < height[1] ? height[0] : height[1];
        }
        int area = 0;
        int left = 0;
        int right = height.length - 1;
        while(left < right){
            int w = right - left;
            int h = Math.min(height[left], height[right]);
            area = Math.max(area, (h *w));
            if(height[left] < height[right]){
                left++;
            }
            else if(height[left] > height[right]){
                right--;
            }
            else {
                left++;
                right--;
            }
        }
        return area;
    }
}
