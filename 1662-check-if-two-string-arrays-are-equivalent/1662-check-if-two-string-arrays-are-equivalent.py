class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        w1,w2=0,0
        i1,i2=0,0

        while w1 <len(word1) and w2 < len(word2):
            if word1[w1][i1] != word2[w2][i2]:
                return False
            

            i1 += 1
            i2 += 1

            if i1 == len(word1[w1]):
                w1 += 1
                i1 = 0
            if i2 ==len(word2[w2]):
                w2 += 1
                i2 =  0
        return w1 == len(word1) and w2 ==len(word2)


        