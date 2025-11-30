# String Compression (https://leetcode.com/problems/string-compression/)
# Difficulty: Medium
# Tags: Two Pointers, String

import math
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0, 0
        n = len(chars)
        while read < n:
            char = chars[read]
            count = 0
            while read < n and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        #del chars[write:]
        return write

    
solution = Solution()

test_cases = [
    (["a","a","b","b","c","c","c"]),                        #6
    (["a"]),                                                #1
    (["a","b","b","b","b","b","b","b","b","b","b","b","b"]) #4
]

for chars in test_cases:
    print(solution.compress(chars))
    print(chars)
