class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[len(piles) - 1]
        while left <= right:
            mid = (left+right) // 2
            acc= 0
            for num in piles:
                mog = (num + mid - 1) // mid 
                acc = acc+mog
            #check to see if current k works:
            if acc > h:
                left = mid+1
            if acc <= h:
                right = mid-1
                minK = mid
        return minK