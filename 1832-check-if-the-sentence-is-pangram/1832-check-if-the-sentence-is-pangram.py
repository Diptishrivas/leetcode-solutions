class Solution(object):
    def checkIfPangram(self, sentence):
        seen =[False]*26
        count=0

        for ch in sentence:
            idx=ord(ch)-ord('a')
            if not seen[idx]:
                seen[idx]=True
                count +=1
                if count ==26:
                    return True
        return count==26
        