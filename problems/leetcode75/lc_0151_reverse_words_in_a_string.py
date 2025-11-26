# Reverse Words in a String (https://leetcode.com/problems/reverse-words-in-a-string/)
# Difficulty: Medium
# Tags: Two Pointers, String

import re

class Solution1:
    def reverseWords(self, s: str) -> str:
        s = re.sub(r"\s+", " ", s.strip()).split(" ")
        s.reverse()
        return " ".join(s)
    
class Solution2:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(re.sub(r"\s+", " ", s.strip()).split(" ")))
    
class Solution3:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
    
solution1 = Solution1()
solution2 = Solution2()
solution3 = Solution3()

test_cases = [
    ("the sky is blue"), #"blue is sky the"
    ("  hello world  "), #"world hello"
    ("a good   example") #"example good a"
]

for s in test_cases:
    print(solution1.reverseWords(s))
for s in test_cases:
    print(solution2.reverseWords(s))
for s in test_cases:
    print(solution3.reverseWords(s))