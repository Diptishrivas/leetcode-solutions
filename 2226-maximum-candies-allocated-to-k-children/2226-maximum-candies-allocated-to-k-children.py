class Solution(object):
    def maximumCandies(self, candies, k):
        
        left = 1
        right = sum(candies) // k

        while left <= right:
            mid = (left + right) // 2

            chunks = 0

            for candy in candies:
                chunks += candy // mid

            if chunks >= k:
                left = mid + 1
            else:
                right = mid - 1

        return right