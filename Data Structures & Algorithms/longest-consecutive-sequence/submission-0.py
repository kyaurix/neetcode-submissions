class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        output = 0
        for i in range(len(nums)):
            seq = 1
            if not (nums[i] - 1) in numSet:
                j = 1
                while (nums[i] + j) in numSet:
                    seq += 1
                    j+=1
                if seq > output:
                    output = seq
        return output



        