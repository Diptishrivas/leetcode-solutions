class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        f={}

        for ch in s:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1

        ans=0
        odd=False

        for count in f.values():
            ans+=(count//2)*2
            
            if count%2==1:
                odd=True
        if odd:
            ans+=1
        return ans
