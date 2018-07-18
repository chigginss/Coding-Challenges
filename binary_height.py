""" 

Find the height of a binary tree using recurusion 

Assume tree is given, root is given, right is given, left is given

If root is None, return -1


"""


def tree_height(root):
    lsum = 0 
    rsum = 0 

    if root is not None:
        lsum = tree_height(root.left)
            lsum += 1
        rsum = tree_height(root.right)
                rsum += 1
        max_sum = max(rsum, lsum)
    else:
        return -1

    return max_sum
