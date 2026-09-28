class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given a list of integers, return a list of the two numbers
        # that add up to the target

        prevMap = {} # val = index
        # enumerate i: index n: number at that index 
        for i, n in enumerate(nums): 
            # find number needed to reach target
            diff = target - n
            # check if we already seen that needed number
            if diff in prevMap:
                # return its saved index and the current index
                return [prevMap[diff], i]
            # save current number and its index for later
            prevMap[n] = i 
