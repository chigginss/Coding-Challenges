
"""Find Mode in BST 

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.



"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # need to search through binary tree and add all nodes into a dictionary
        # the key of the dictionary is the node value, the value of the dictionary is the count of that val in tree
        # then return the k,v pair with the highest value 
        
        current = self
        all_nodes = {}
        
        if current is not None and not in all_nodes:
            all_nodes[current] = 1
        elif current is not None and in all_nodes:
            all_nodes[current] += 1
        findMode(current.left)
        findMode(current.right)
        
        return 
        
        
#         while current:
#             if current not in all_nodes: 
#                 all_nodes[current] = 1
#             else: 
#                 all_nodes[current] += 1
#             current = current.left
        
#         while current:
#             if current not in all_nodes:
#                 all_nodes[current.val] = 1
#             else: 
#                 all_nodes[current.val] += 1
#             current = current.right
        
#         print all_nodes
        
#         for item in pairs:
#             max_num = 0 
#             if item[1] > max_num:
#                 item[1] = max_num
        
#         if item[1] == max_num:
#             return [item[0]]
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        self.morrisTraversal(root,d)
        if not d:
            return []
                        
        # Find the max element in the dictionary with values
        m = max(d.values())
                
        # Now returns All keys having this m as its value
        return [ k for k,v  in d.items() if v == m ]


    # The whole idea of morris traversal is to find a way back to the root node 
    # after going left, that is what recursion does is it automatically using
    # stack push/pop find a way back to current node after traversing left child.
    # but to do it without recursion, we need to find the inorder predecessor of the 
    # current node and link that predecessor to the current node.
        
        
    def morrisTraversal(self,root,d):
        if not root:
            return None
        
        current = root
        
        while current:
                
            # Check to see if lef of current is none, if yes than print the current and
            # Move to right subtree
            if not current.left:
                d[current.val] += 1
                current = current.right
                                
            # If current has left child than we need to find the predecessor of the
            # current node
            else:
                pre = current.left
                                
                # move to the right most element, that should be the predecessror of the 
                # current node
                while pre.right and pre.right != current:
                    pre = pre.right
                    
                # Now link this pre node to the current node, also remember if pre.right is not NOne yet
                # than that means we have already found the predecessor of the node
                if not pre.right:
                    pre.right = current
                                        
                    # lets move to left child as we have found the predecessor and linked it as well
                    current = current.left
                                        
                # Revert or disable the link that we have formed during morris traversal
                else:
                    pre.right = None
                    d[current.val] += 1
                    current = current.right
 

