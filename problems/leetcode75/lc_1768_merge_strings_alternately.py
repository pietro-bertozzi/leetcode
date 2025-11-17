# Merge Strings Alternately (https://leetcode.com/problems/merge-strings-alternately/)
# Difficulty: Easy
# Tags: Two Pointers, String

from itertools import zip_longest

class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longer, shorter = (word1, word2) if len(word1) > len(word2) else (word2, word1)
        merged = ''
        for i in range(len(shorter)):
            merged += word1[i] + word2[i]
        merged += longer[len(shorter):]
        return merged
    
class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
    
solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ("abc", "pqr"), #apbqcr
    ("ab", "pqrs"), #apbqrs
    ("abcd", "pq")  #apbqcd
]

for word1, word2 in test_cases:
    print(solution1.mergeAlternately(word1, word2))
for word1, word2 in test_cases:
    print(solution2.mergeAlternately(word1, word2))