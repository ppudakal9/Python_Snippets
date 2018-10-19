class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        # """
        # :type root: TreeNode
        # :rtype: List[int]
        # """
        arr = []

        if root != None:
            return self._inorderTraversal(root, arr)

        return arr

    def _inorderTraversal(self, currNode, arr):
        if currNode != None:
            self._inorderTraversal(currNode.left, arr)
            arr.append(currNode.val)
            self._inorderTraversal(currNode.right, arr)

        return arr