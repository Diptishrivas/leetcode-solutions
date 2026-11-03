class Solution(object):
    def fib(self, n):
        
        dp={}
        def fun(n):
            if n==0 or n==1:
                return n
            if n in dp:
                return dp[n]
       
            a=fun(n-1)
            b=fun(n-2)

            ans=a+b

            dp[n]=ans

            return ans    

        return fun(n)

