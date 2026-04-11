# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        result =[]
        

        def dfs(node):

            if not node:
                return

            left_child = dfs(node.left)

            if left_child:

                result.append(left_child.val)

            if node:
                
                result.append(node.val)
            
            right_child = dfs(node.right)

            if right_child:

                result.append(right_child.val)

        dfs(root)

        return result[k-1]