class Solution {
    public int removeDuplicates(int[] nums) {
        int l = nums.length;
        if(l>0){
            for(int i=0; i<l-1; i++){
                if(nums[i]==nums[i+1]){
                    for(int j=i; j<l-1; j++){
                        nums[j] = nums[j+1];
                    }
                    l--;
                    i--;
                }
            }
        }
        return l;
    }
}