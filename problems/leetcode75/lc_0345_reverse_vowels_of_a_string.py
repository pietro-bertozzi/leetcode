# Reverse Vowels of a String (https://leetcode.com/problems/reverse-vowels-of-a-string/)
# Difficulty: Easy
# Tags: Two Pointers, String
    
class Solution1:
    def reverseVowels(self, s: str) -> str:
        indexes = []
        values = []
        vowels = "aeiou"
        for i in range(len(s)):
            if s[i].lower() in vowels:
                indexes.append(i)
                values.append(s[i])
        values.reverse()
        chars = list(s)
        for i in range(len(indexes)):
            chars[indexes[i]] = values[i]
        return "".join(chars)

class Solution2:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        chars = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and chars[l] not in vowels:
                l += 1
            while l < r and chars[r] not in vowels:
                r -= 1
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        return ''.join(chars)

solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ("IceCreAm"), #"AceCreIm"
    ("leetcode"), #"leotcede"
]

for s in test_cases:
    print(solution1.reverseVowels(s))
for s in test_cases:
    print(solution2.reverseVowels(s))