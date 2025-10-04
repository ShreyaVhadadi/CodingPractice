class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,curr,total):
            if target==total:
                res.append(curr.copy())
                return
            if i==len(nums) or total>target:
                return
            curr.append(nums[i])
            dfs(i,curr,total+nums[i])
            curr.pop()
            dfs(i+1,curr,total)

        dfs(0,[],0)
        return res
        #TC:O(2^t/m)
        #SC:O(t/m)


        
