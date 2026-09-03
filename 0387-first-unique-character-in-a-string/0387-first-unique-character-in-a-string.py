class Solution(object):
    def firstUniqChar(self, s):
        
        f={}

        for i in range (len(s)):
            if s[i] in f:
                f[s[i]] +=1
            else:
                f[s[i]]=1
        
        for i in range (len(s)):
            if f[s[i]] ==1:
                return i
                
        return -1