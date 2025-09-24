# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def preorder(root):
            if not root:
                res.append("Null")
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals=data.split(",")
        self.i=0
        def dfs():
            if vals[self.i] == "Null":
                self.i+=1
                return None
            curr=TreeNode(int(vals[self.i]))
            self.i+=1
            curr.left=dfs()
            curr.right=dfs()
            return curr
        return dfs()
            







