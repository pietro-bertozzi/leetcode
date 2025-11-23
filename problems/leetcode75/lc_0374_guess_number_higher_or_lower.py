# Guess Number Higher or Lower (https://leetcode.com/problems/guess-number-higher-or-lower/)
# Difficulty: Easy
# Tags: Binary Search, Interactive

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    picked = None

    def guess(self, num: int) -> int:
        global picked
        if num > picked:
            return -1
        elif num < picked:
            return 1
        else:
            return 0
    
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (right+left)//2
            response = self.guess(mid)
            if response == -1:
                right = mid - 1
            elif response == 1:
                left = mid + 1
            else:
                return mid

solution = Solution()

test_cases = [
    (10, 6), #6
    (1, 1),  #1
    (2, 1)   #1
]

for n, num in test_cases:
    picked = num
    print(solution.guessNumber(n))
