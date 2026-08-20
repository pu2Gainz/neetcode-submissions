# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(curr, depth):
            if not curr:
                return None
            if depth == len(res):
                res.append(curr.val)

            dfs(curr.right, 1 + depth)
            dfs(curr.left, 1 + depth)

        dfs(root, 0)

        return res