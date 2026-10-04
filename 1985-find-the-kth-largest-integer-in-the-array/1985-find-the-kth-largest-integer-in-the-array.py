class Solution(object):
    def kthLargestNumber(self, nums, k):
         
        min_heap = []

        for num in nums:
            item = (len(num), num)
            heapq.heappush(min_heap, item)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0][1]