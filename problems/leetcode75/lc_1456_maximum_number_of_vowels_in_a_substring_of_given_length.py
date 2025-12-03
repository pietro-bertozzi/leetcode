# Maximum Number of Vowels in a Substring of Given Length (https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
# Difficulty: Medium
# Tags: String, Sliding Window

class Solution1:
    def maxVowels(self, s: str, k: int) -> int:
        best, candidate = 0, 0
        vowels = set("aeiou")
        for i in range(k):
            if s[i] in vowels:
                candidate += 1
        best = candidate
        for i in range(k, len(s)):
            if s[i] in vowels:
                candidate += 1
            if s[i - k] in vowels:
                candidate -= 1
            if candidate > best:
                best = candidate
        return best

class Solution2:
    def maxVowels(self, s: str, k: int) -> int:
        best, candidate = 0, 0
        vowels = set('aeiou')
        for i, c in enumerate(s):
            if c in vowels:
                candidate += 1
            if i >= k and s[i - k] in vowels:
                candidate -= 1
            if candidate > best:
                best = candidate
        return best
        
solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ("abciiidef", 3), #3
    ("aeiou", 2),     #2
    ("leetcode", 3)   #2
]

for s, k in test_cases:
    print(solution1.maxVowels(s, k))
for s, k in test_cases:
    print(solution2.maxVowels(s, k))