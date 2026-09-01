class Solution(object):
    def isHappy(self, n):

        def fun(n):
            total=0

            while n>0:
                digit = n%10
                total += digit*digit
                n=n//10

            return total

            

        slow=n
        fast=n

        while fast!=1:
            slow=fun(slow)
            fast=fun(fun(fast))

            if fast==1:
                return True

            if slow==fast:
                return False

        return True

        
             

       