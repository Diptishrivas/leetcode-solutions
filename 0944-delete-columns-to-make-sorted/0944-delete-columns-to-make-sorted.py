class Solution(object):
    def minDeletionSize(self, strs):
        delete_count= 0
        nums_row= len(strs)
        nums_cols=len(strs[0])

        for i in range(nums_cols):
            for j in range(nums_row-1):
                if strs[j][i]> strs[j+1][i]:
                    delete_count += 1
                    break
        return delete_count
        