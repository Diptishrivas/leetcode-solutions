class Solution(object):
    def findSubstring(self, s, words):
       
        from collections import Counter

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_count = Counter(words)
        result = []

        for i in range(word_len):

            left = i
            right = i
            seen = {}
            count = 0

            while right + word_len <= len(s):

                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        result.append(left)

                else:
                    seen.clear()
                    count = 0
                    left = right

        return result