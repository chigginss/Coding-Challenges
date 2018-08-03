# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if not t1 or t2:
            return t1 or t2
        
        #create one node from both trees
        root = TreeNode(t1.val + t2.val)
        rootArr = [root]
        t1Arr = [t1]
        t2Arr = [t2]
        
        # use pop to get singular values from t1 and t2
        while t1Arr and t2Arr:
            node = rootArr.pop()
            n1 = t1Arr.pop()
            n2 = t2Arr.pop()
        
        
        
        
            
  def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 or not t2:
            return t1 or t2
        root = TreeNode(t1.val + t2.val)
        treeArr = [root]
        treeArr1 = [t1]
        treeArr2 = [t2]
        
        while treeArr1 and treeArr2:
            node = treeArr.pop()
            node1 = treeArr1.pop()
            node2 = treeArr2.pop()
            if node1.left and node2.left:
                node.left = TreeNode(node1.left.val + node2.left.val)
                treeArr.append(node.left)
                treeArr1.append(node1.left)
                treeArr2.append(node2.left)
            else:
                if not node1.left:
                    node.left = node2.left
                else:
                    node.left = node1.left
            if node1.right and node2.right:
                node.right = TreeNode(node1.right.val + node2.right.val)
                treeArr.append(node.right)
                treeArr1.append(node1.right)
                treeArr2.append(node2.right)
            else:
                if not node1.right:
                    node.right = node2.right
                else:
                    node.right = node1.right
        treeArr.clear()
        return root      
        
        
    def traverseTrees(self, t1, t2)
        new_tree = set()
        
        if self.root is None:
            return None
        
        while self.left in t1 is not None:
            new_tree.add(self.val)
            self.left = self.left.left
        
        while self.right in t1 is not None:
            new_tree.add(self.val)
            self.right = self.right.right
        
        while self.left in t2 is not None:
            new_tree.add(self.val)
            self.left = self.left.left
            
        while self.right in t2 is not None:
            new_tree.add(self.val)
            self.right = self.right.right
            
        for item in new_tree:
            
            
        