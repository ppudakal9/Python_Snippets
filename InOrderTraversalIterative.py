class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        temp = []

        flag = True

        currNode = root

        while flag:
            if currNode != None:
                temp.append(currNode)
                currNode = currNode.left
            else:
                if len(temp) > 0:
                    currNode = temp.pop()
                    arr.append(currNode.val)
                    currNode = currNode.right
                else:
                    flag = False

        return arr
