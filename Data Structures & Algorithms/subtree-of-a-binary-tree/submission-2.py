# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def isSameTree(s1, s2):

            if not s1 and not s2:
                return True

            #Remove s1 in if check, since i need to check only till s2 exists

            if  s1 and s2 and s1.val ==s2.val:
                return isSameTree(s1.left, s2.left) and isSameTree(s1.right, s2.right)
            else:
                return False


        def dfs(node):

            if not node:
                return False

            if isSameTree(node, subRoot):
                return True 

            else:

                return dfs(node.left) or dfs(node.right)

            

        return dfs(root)
