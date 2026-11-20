class NumArray:

    def __init__(self, nums: List[int]):
        c = 0
        self.prefix = []

        for num in nums:
            c += num
            self.prefix.append(c)

    def sumRange(self, left: int, right: int) -> int:
        rsum = self.prefix[right]
        lsum = self.prefix[left - 1] if left > 0 else 0
        return rsum - lsum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)