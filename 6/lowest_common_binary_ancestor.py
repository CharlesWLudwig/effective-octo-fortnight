# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or matches p/q, return root
        if not root or root == p or root == q:
            return root
        
        # Recursively search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both subtrees return non-null, current root is LCA
        if left and right:
            return root
        
        # Propagate the non-null result upwards
        return left if left else right
