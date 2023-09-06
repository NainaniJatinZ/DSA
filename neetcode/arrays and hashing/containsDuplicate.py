class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # learned about hash set, 
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False
        
        # # Stupid Try 1
        # hash1 = {}
        # # print(hash1[1])
        # for i in nums:
        #     try:
        #         if hash1[i] == 1:
        #             return True
        #     except Exception as e:
        #         print(e)
        #     hash1[i] = 1
        # return False


        