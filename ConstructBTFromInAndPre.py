class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, pre_order, in_order):

        if len(pre_order) == 0:
            if len(in_order) == 0:
                return None
            else:
                return in_order[0]

        root = TreeNode(pre_order[0])
        print(root.val)
        for i in range(0, len(in_order)):
            if in_order[i] == root.val:
                idx = i
                break

        root.left = self.buildTree(pre_order[1:idx], in_order[:idx])
        print(root.left)
        root.right = self.buildTree(pre_order[idx+1:], in_order[idx+1:])
        print(root.right)
        return root


pre = [3,9,20,15,7]
in_ord = [9,3,15,20,7]
obj = Solution()
obj.buildTree(pre, in_ord)