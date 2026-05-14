class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        empty_set = set(nums)

        curr = 1

        while True:
            if curr not in empty_set:
                return curr
            curr += 1
