class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # forgot to check for length
        # .get() on dict has alternate param, for when the key doesnt exist
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        
        return hash_s == hash_t
        
        # try 1, not bad tbh, just missing syntax 
        # hash_s = {}
        # hash_t = {}
        # for i in s:
        #     if i in hash_s.keys():
        #         hash_s[i] += 1
        #     else:
        #         hash_s[i] = 1
        # for j in t:
        #     if j in hash_t.keys():
        #         hash_t[j] += 1
        #     else:
        #         hash_t[j] = 1
        # print(hash_s)
        # print(hash_t)
        # if hash_s == hash_t:
        #     return True
        # return False
        

