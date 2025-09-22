    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root,subRoot)->bool:
            if not root:
                return False
            if(root.val==subRoot.val):
                if (isMatch(root,subRoot)):
                    return True
            return isEqual(root.left,subRoot) or isEqual(root.right,subRoot)

        def isMatch(root,subRoot)->bool:
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val!=subRoot.val:
                return False
            return isMatch(root.left,subRoot.left) and isMatch(root.right,subRoot.right)
        
        flag=isEqual(root,subRoot)
        return flag
        # TC:O(M*N)
        # SC:O(M+N)
