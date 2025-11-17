# Greatest Common Divisor of Strings (https://leetcode.com/problems/greatest-common-divisor-of-strings/)
# Difficulty: Easy
# Tags: Math, String

from math import gcd

class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_len = gcd(len(str1), len(str2))
        for i in range(max_len, 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                if str1[:i] * (len(str1) // i) == str1 and str1[:i] * (len(str2) // i) == str2:
                    return str1[:i]
        return ''
                
class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        length_gcd = gcd(len(str1), len(str2))
        return str1[:length_gcd]
    
solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ("ABCABC", "ABC"),  #"ABC"
    ("ABABAB", "ABAB"), #"AB"
    ("LEET", "CODE")    #""
]

for str1, str2 in test_cases:
    print(solution1.gcdOfStrings(str1, str2))
for str1, str2 in test_cases:
    print(solution2.gcdOfStrings(str1, str2))