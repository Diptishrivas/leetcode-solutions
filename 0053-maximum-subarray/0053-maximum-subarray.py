class Solution(object):
    def maxSubArray(self, nums):

        max_sum=current_sum=nums[0]

        for num in nums[1:]:
            if current_sum<0:
                current_sum=0
            current_sum=current_sum+num
            max_sum=max(current_sum,max_sum)
        return max_sum
        # bestending = nums[0]
        # ans=nums[0]

        # for i in range(1, len(nums)):
        #     v1=bestending+ nums[i]
        #     v2=nums[i]
         
        #     bestending=max(v1,v2)
        #     ans=max(ans, bestending)
        # return ans

        