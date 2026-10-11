class Solution(object):
    def numberOfBeams(self, bank):
        n = len(bank)
        prev = 0
        next_count = 0
        result = 0

        for i in range(n):
            for j in range(len(bank[i])):
                if bank[i][j] == '1':
                    next_count += 1

            if next_count != 0:
                result += prev * next_count
                prev = next_count
                next_count = 0

        return result