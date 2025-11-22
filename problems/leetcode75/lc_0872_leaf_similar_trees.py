# Leaf-Similar Trees (https://leetcode.com/problems/leaf-similar-trees/)
# Difficulty: Easy
# Tags: Tree, Depth-First Search, Binary Tree

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def all_leaves(self, node: TreeNode | None, leaves: list[int]) -> None:
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
        self.all_leaves(node.left, leaves)
        self.all_leaves(node.right, leaves)

    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        leaves1, leaves2 = [], []
        self.all_leaves(root1, leaves1)
        self.all_leaves(root2, leaves2)
        return leaves1 == leaves2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def next_leaf(self, stack: list[TreeNode]) -> int | None:
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.left and not node.right:
                return node.val
        return None

    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        stack1 = [root1] if root1 else []
        stack2 = [root2] if root2 else []
        while stack1 and stack2:
            leaf1 = self.next_leaf(stack1)
            leaf2 = self.next_leaf(stack2)
            if leaf1 != leaf2:
                return False
        return not stack1 and not stack2

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

solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ([3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]), #True
    ([1,2,3], [1,3,2])                                                                  #False
]

for root1, root2 in test_cases:
    print(solution1.leafSimilar(build_binary_tree(root1), build_binary_tree(root2)))
for root1, root2 in test_cases:
    print(solution2.leafSimilar(build_binary_tree(root1), build_binary_tree(root2)))
