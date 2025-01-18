class Solution {
    public int findClosestNumber(int[] nums) {
       int mindiff=Integer.MAX_VALUE;
       int ans=0;
       int prevdiff=Integer.MAX_VALUE;
       for (int i=0;i<nums.length;i++) 
       {
        int diff=Math.abs(nums[i]-0);
        mindiff=Math.min(mindiff,diff);
        if(diff<prevdiff)
            {ans=nums[i];
            prevdiff=mindiff;}
        else if(diff==prevdiff){
            ans=Math.max(ans,nums[i]);
            prevdiff=mindiff;
        }
       }
       return ans;

    }
}
