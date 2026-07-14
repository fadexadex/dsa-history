class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are None
        if not p and not q:
            return True

        # One node is None and the other isn't
        if not p or not q:
            return False

        # Values are different
        if p.val != q.val:
            return False

        # Recursively compare left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
