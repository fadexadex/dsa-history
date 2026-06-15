# max (1 + 0 +0 , 1+ 0+ 0)  + 1 = 2

# max(2, 1) = 2

# 2 + 1 = 3


def maxDepth(root):

    if root == null:
        return 0
    
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))