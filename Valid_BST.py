import sys

class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def validate_bst(root, min = -sys.maxsize, max = sys.maxsize):
    if root is None:
        return True

    if (root.value > min and root.value < max and validate_bst(root.left, min, root.value) and validate_bst(root.right, root.value, max)):
        return True
    else:
        return False


#Test case:
root = node(5)
root.left = node(4)
root.right = node(6)
print(validate_bst(root))