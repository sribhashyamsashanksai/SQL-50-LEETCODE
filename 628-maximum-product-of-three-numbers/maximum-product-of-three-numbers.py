class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        # The maximum product can be from:
        # 1. The product of the three largest numbers
        max_product1 = nums[-1] * nums[-2] * nums[-3]
        
        # 2. The product of two smallest numbers (could be negative) and the largest number
        max_product2 = nums[0] * nums[1] * nums[-1]
        
        # Return the maximum of both products
        return max(max_product1, max_product2)