class Solution(object):
    def maxSubArray(self, nums):
        bestending = nums[0]
        ans=nums[0]

        for i in range(1, len(nums)):
            v1=bestending+ nums[i]
            v2=nums[i]
         
            bestending=max(v1,v2)
            ans=max(ans, bestending)
        return ans

        