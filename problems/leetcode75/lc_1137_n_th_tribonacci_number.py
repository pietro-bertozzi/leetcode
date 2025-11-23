# N-th Tribonacci Number (https://leetcode.com/problems/n-th-tribonacci-number/)
# Difficulty: Easy
# Tags: Math, Dynamic Programming, Memoization

class Solution1:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        return dp[n]

class Solution2:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        for _ in range(n - 2):
            dp[0], dp[1], dp[2] = dp[1], dp[2], dp[0] + dp[1] + dp[2]
        return dp[2]
  
solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    (4), #4
    (25) #1389537
]

for n in test_cases:
    print(solution1.tribonacci(n))
for n in test_cases:
    print(solution2.tribonacci(n))
