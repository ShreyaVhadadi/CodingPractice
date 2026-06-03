lass Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n=len(coins)
        # dp={}
        # def dfs(i,amt):
        #     if i>=n or amt<0:
        #         return 0
        #     if amt==0:
        #         return 1
        #     if (i,amt) in dp:
        #         return dp[(i,amt)]
        #     res=dfs(i+1,amt)
        #     if amt>=coins[i]:
        #         res+=dfs(i,amt-coins[i])
        #     dp[(i,amt)]=res
        #     return res
        
        # return dfs(0,amount)
        #TC:O(M*N)
        #SC:O(M*N)

        #Bottom up optimized
        n=len(coins)
        dp=[0]*(amount+1)
        dp[0]=1    
        # newnextdp=[0]*(amount+1) 
        # newnextdp[0]=1
        for i in range(n-1,-1,-1):
            nextdp=[0]*(amount+1)
            nextdp[0]=1
            for a in range(amount+1):
                nextdp[a]=dp[a]#dp is i+1
                if a>=coins[i]:                   
                    nextdp[a]+=nextdp[a-coins[i]]#nextdp = i same row
            dp=nextdp
        return dp[amount]
        #TC: O(n*a)
        #SC:O(a)
