# Is Subsequence (https://leetcode.com/problems/is-subsequence/)
# Difficulty: Easy
# Tags: Two Pointers, String, Dynamic Programming

class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):
                    return True
        return False
class Solution2:
    def isSubsequence(self, s: str, t: str):
        it = iter(t)
        return all(c in it for c in s)

solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ("abc", "ahbgdc"), #True
    ("axc", "ahbgdc"), #False
]

for s, t in test_cases:
    print(solution1.isSubsequence(s, t))
for s, t in test_cases:
    print(solution2.isSubsequence(s, t))