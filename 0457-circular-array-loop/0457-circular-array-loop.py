class Solution(object):
    def circularArrayLoop(self, nums):
        
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        def same_direction(i, j):
            return (nums[i] > 0) == (nums[j] > 0)

        for i in range(n):

            slow = i
            fast = i

            while True:

                 
                next_slow = next_index(slow)

                
                if not same_direction(i, next_slow):
                    break

               
                slow = next_slow

                
                next_fast = next_index(fast)

                if not same_direction(i, next_fast):
                    break

                
                next_fast = next_index(next_fast)

                if not same_direction(i, next_fast):
                    break

                fast = next_fast

                
                if slow == fast:

                 
                    if slow == next_index(slow):
                        break

                    return True

        return False