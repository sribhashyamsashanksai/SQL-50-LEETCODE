class Solution:
    def maxSubArray(self, nums):
        curmax=0
        maxtillnow=-inf
        for c in nums:
            curmax=max(c,c+curmax)
            maxtillnow=max(curmax,maxtillnow)
        return maxtillnow