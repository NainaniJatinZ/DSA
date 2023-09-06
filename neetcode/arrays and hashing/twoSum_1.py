class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # failed to use hashmap correctly
        hashmap = {} # value - keys, index - value

        for ind, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], ind] 
            hashmap[val] = ind       

        # try 1, slow but memory efficient, beats 90% on memory
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i, j]


        