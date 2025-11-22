# Maximum Depth of Binary Tree (https://leetcode.com/problems/maximum-depth-of-binary-tree/)
# Difficulty: Easy
# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

def build_binary_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i >= len(values):
            break
        if values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

solution = Solution()

test_cases = [
    ([3,9,20,None,None,15,7]), #3
    ([1,None,2])               #2
]

for root in test_cases:
    print(solution.maxDepth(build_binary_tree(root)))
