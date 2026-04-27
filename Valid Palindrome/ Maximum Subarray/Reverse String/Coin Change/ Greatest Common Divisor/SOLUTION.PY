class Solution:
    def findGCD(self, nums):
        small = min(nums)
        large = max(nums)

        while small:
            large, small = small, large % small

        return large
