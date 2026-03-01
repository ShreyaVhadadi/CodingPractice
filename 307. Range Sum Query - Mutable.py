class SegmentNode:
    __init__(self,start,end,sum):
    self.start=start
    self.end=end
    self.total=total
    self.left=Null
    self.right=Null

    @static method
    def create(start,end,nums):
        if start==end:
            return SegmentNode(start,end,nums[start])
        root=SegmentNode(start,end,0)
        mid=start+end//2
        root.left=create(root.start,mid,nums)
        root.right=create(mid+1,root.end,nums)
        root.sum=root.left.sum+root.right.sum
        return root


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        # self.start=0
        # self.end=len(nums)
        root=SegmentNode.create(self.start,self.end,self.nums)


    def update(self, index: int, val: int) -> None:
        if rootindex

        

    def sumRange(self, left: int, right: int) -> int:
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
