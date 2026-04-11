class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
    # U: given a list of integers, want to find integers that
    # are duplicates, output t/f

    # P: use a hashmap to store the numbers,
    # if we see that same number in the hashmap, return True
    # otherwise append and keep adding number

        hashmap = []

        for num in nums:
            if num in hashmap:
                return True
            hashmap.append(num)
        return False