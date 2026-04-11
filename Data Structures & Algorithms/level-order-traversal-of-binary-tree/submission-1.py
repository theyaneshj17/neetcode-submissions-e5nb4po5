# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result =[]
        que = deque([root])

        if not root:
            return result
        

        while que:

            length = len(que)

            current=[]

            for i in range(length):

                

                node = que.popleft()

                current.append(node.val)

                if node.left:

                    que.append(node.left)

                if node.right:

                    que.append(node.right)

            result.append(list(current))

        return result






        