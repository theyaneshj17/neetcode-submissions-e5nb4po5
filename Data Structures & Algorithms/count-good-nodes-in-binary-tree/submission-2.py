# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        value = root.val

        result =0

    

        def dfs(node, max_so_far):

            nonlocal result

            if not node:
                return

            #Scan till bottom or leaft of path, i need to find

            if node.val >= max_so_far: #and node.val > value:

                result+=1

            

            dfs(node.left, max(max_so_far, node.val))

            dfs(node.right, max(max_so_far, node.val))

        
        dfs(root, float('-inf'))

        return result
        