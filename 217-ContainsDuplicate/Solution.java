class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> visited = new HashSet<Integer>();
        for (int val : nums){
            if(visited.contains(val)){
                return true;
            }
            else{
                visited.add(val);
            }
        }
        return false;
    }
}
