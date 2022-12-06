class Solution:
    def inorderTraversal(self,root):
        def helper(root):
            if root == None:
                return
            helper(root.left)
            rst.append(root.val)
            helper(root.right)
            return
        rst = []
        helper(root)
        return rst
