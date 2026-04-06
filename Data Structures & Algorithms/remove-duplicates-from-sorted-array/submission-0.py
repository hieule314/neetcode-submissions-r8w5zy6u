class Solution:
    # U: given a list of nondecreasing 
    # order of integers
    # output number of unique elements

    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # first element is always unique
        # start from 1 to all of nums
        for i in range(1, len(nums)):
            # if current num != num before,
            # unique element found
            if nums[i] != nums[i-1]:
                # Found unique element
                nums[k] = nums[i]
                # increment # of unique elements
                k += 1 

        return k
        