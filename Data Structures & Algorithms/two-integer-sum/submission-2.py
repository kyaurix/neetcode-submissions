class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complementVal = target - nums[i]
            if complementVal in seen:
                return [seen[complementVal], i]
            else:
                seen[nums[i]] = i
