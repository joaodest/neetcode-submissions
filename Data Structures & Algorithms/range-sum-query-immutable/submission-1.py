class NumArray:

    def __init__(self, nums: List[int]):
        self.mem = {k: v for k, v in enumerate(nums)}

    def sumRange(self, left: int, right: int) -> int:
        sub_idx = list(self.mem.keys())
        res = 0
        for i in sub_idx[left:right + 1]:
            res += self.mem[sub_idx[i]]

        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)