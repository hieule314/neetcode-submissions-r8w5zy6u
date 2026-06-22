class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [] # initialize empty list
        for i in nums * 2:
            result.append(i)
        return result