class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    # Base case if it's a leaf node (i.e., has no children)
    if not root:
        return None
    # Swap children of top-level node
    root.left, root.right = root.right, root.left
    
    # Recurisvely invert children subtrees 
    # Use the function recursively to solve similar instance of the same problem 
    # This is called recursion
    invertTree(root.left)
    invertTree(root.right)
    return root

# This is a Depth-First Search 
