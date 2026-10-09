class Solution(object):
    def compress(self, chars):
        j = 0
        count = 1

        for i in range(len(chars)):
            if i == len(chars) - 1 or chars[i] != chars[i + 1]:
                chars[j] = chars[i]
                j += 1

                if count > 1:
                    for digit in str(count):
                        chars[j] = digit
                        j += 1

                count = 1
            else:
                count += 1

        return j

                    
        