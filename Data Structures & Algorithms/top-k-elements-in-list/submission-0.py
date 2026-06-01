class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyCount = {}
        for i in range (len(nums)):
            if nums[i] in frequencyCount:
                frequencyCount[nums[i]] = frequencyCount[nums[i]] + 1
            else:
                frequencyCount[nums[i]] = 1
        return sorted(frequencyCount, key=frequencyCount.get, reverse=True)[:k]