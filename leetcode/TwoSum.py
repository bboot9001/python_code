class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        countfirst  = 0
        countsecond = 0
        for a in range(len(nums)):
            countsecond = countfirst + 1
            for b in range(len(nums) - countfirst - 1):
                if nums[countfirst] + nums[countsecond] == target:
                    return (countfirst,countsecond)
                else:
                    countsecond+=1
            countfirst+=1


target1 = 6
nums1 = [3,2,4]

s = Solution()
r = s.twoSum(nums1,target1)
