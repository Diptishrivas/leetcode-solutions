class Solution(object):
    def distributeCandies(self, candyType):
        
        different=len(set(candyType))
        half=len(candyType)//2

        return min(different,half)