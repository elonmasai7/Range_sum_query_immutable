class NumArray(object):
    def __init__(self, nums):
        self.prefixSum = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            self.prefixSum[i] = self.prefixSum[i - 1] + nums[i - 1]

    def sumRange(self, left, right):
        return self.prefixSum[right + 1] - self.prefixSum[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])

print(numArray.sumRange(0, 2))  
print(numArray.sumRange(2, 5))  
print(numArray.sumRange(0, 5))  
