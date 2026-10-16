class Solution(object):
    def countAndSay(self, n):
      
        result = "1"

        for i in range(n - 1):
            ans = ""
            count = 1

            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    ans += str(count) + result[j - 1]
                    count = 1

            ans += str(count) + result[-1]
            result = ans

        return result