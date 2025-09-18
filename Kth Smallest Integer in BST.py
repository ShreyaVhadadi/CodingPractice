# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        stack=[]
        curr=root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            count+=1
            if k==count:
                return curr.val
            curr=curr.right
        return curr.val
        #TC:O(N)
        #SC:O(H)
