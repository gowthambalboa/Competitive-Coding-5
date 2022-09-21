# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):
        if root is None: return []
        q = []
        levels = []
        ans = []
        q.append(root)
        while q:
            size = len(q)
            temp = []
            for i in range(size):
                e = q.pop(0)
                temp.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            levels.append(temp)
        for level in levels:
            ans.append(max(level))
        return ans
        
        