def kthsmall(root, k):
    counter = 0 
    res = 0 

    def inorder(node):
        if not root:
            return
         inorder(node.left)
         counter += 1
             if counter == k:
                res = node.val 
                return
        inorder(node.right)
    inorder(root)
    return res
