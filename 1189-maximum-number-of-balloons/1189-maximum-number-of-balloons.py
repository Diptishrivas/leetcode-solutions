class Solution(object):
    def maxNumberOfBalloons(self, text):
        
        f={}

        for ch in text:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1
        
        return min(
            f.get('b',0),
            f.get('a',0),
            f.get('l',0)//2,
            f.get('o',0)//2,
            f.get('n',0)
        )