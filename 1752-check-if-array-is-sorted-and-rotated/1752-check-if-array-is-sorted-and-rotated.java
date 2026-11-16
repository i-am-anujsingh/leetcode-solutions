class Solution {
    public boolean check(int[] nums) {
        boolean f = false;
        int l = nums.length;
        int cp[] = Arrays.copyOf(nums, l);
        
        Arrays.sort(cp);

        for(int i=0; i<l; i++){
            int p = nums[0];
            for(int j=0; j<l-1; j++){
                nums[j] = nums[j+1];
            }

            nums[l-1] = p;

            if(Arrays.equals(nums, cp)){
                f = true;
                break;
            }
        }
        return f;
    }
}