# Search in a Binary Search Tree (https://leetcode.com/problems/search-in-a-binary-search-tree/)
# Difficulty: Easy
# Tags: Tree, Binary Search Tree, Binary Tree

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return None
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)
        return root

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
    ([4,2,7,1,3], 2), #[2,1,3]
    ([4,2,7,1,3], 5)  #[]
]

for root, val in test_cases:
    print(solution.searchBST(build_binary_tree(root), val))
