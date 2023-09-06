class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use maps here
        # you can identify anagrams with sorted string too 
        newMap = defaultdict(list) #like dict() but doesnt raise KeyError if key doesnt exist
        for z in strs:
            sorting = ''.join(sorted(z))        #unique identifier
            newMap[sorting].append(z)           
        return list(newMap.values())
        
        # try 1 failed, was trying to create a hash map, freq count of each string, couldnt keep that as dictionary key
        # crazy_list = []
        # crazy_dict = {}
        # for i in strs:
        #     temp_dict = {}
        #     for j in i:
        #         temp_dict[j] = 1 + temp_dict.get(j, 0)
        #     crazy_dict[i] = temp_dict 
        
        # dict_list = list(crazy_dict.keys())
        # for k in range(len(dict_list)):
        #     if any(dict_list[k] in crazy_sub_list for crazy_sub_list in crazy_list):
        #         continue
        #     temp_list = [dict_list[k]]
        #     for h in range(k+1, len(dict_list)):
        #         if crazy_dict[dict_list[k]] == crazy_dict[dict_list[h]]:
        #             temp_list.append(dict_list[h])
        #     crazy_list.append(temp_list)
        # return crazy_list
        
        
