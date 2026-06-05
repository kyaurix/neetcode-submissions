class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        output = 0
        for num in numSet:
            seq = 1
            if not (num-1) in numSet:
                j = 1
                while (num+j) in numSet:
                    seq += 1
                    j+=1
                if seq > output:
                    output = seq
        return output



        